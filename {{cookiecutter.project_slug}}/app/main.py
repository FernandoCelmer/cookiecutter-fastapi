from typing import Annotated

from fastapi import Depends, FastAPI
{%- if cookiecutter.use_serverless == 'y' %}
from mangum import Mangum
{%- endif %}

from app import __version__
from app.core.settings import Settings
{%- if cookiecutter.use_auth == 'y' %}
from app.core.auth.endpoints import auth
{%- endif %}
from app.api.v1.routers import router


app = FastAPI(
    title="Test FastAPI Template",
    description="Amazing project with FastAPI!",
    version=__version__
)

{%- if cookiecutter.use_auth == 'y' %}

app.include_router(auth, prefix="/auth")
{%- endif %}
app.include_router(router, prefix="/v1")

{%- if cookiecutter.use_serverless == 'y' %}

handler = Mangum(app)
{%- endif %}


# TODO: Test Config!
@app.get("/info")
async def info(settings: Annotated[Settings, Depends(Settings.get_settings)]):
    return {
        "scope": settings.scope,
        "database_url": settings.database_url
    }
