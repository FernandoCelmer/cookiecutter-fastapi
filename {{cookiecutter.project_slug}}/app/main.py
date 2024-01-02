from os import getenv
from functools import lru_cache
from typing import Annotated

from fastapi import Depends, FastAPI
{%- if cookiecutter.use_serverless == 'y' %}
from mangum import Mangum
{%- endif %}

from app import __version__
from app.core.settings import Base
from app.api.v1.routers import router


@lru_cache
def get_settings():
    environment = getenv("SCOPE", "test").lower()
    return getattr(Base, environment)()


app = FastAPI(
    title="{{ cookiecutter.project_name }}",
    description="{{ cookiecutter.description }}",
    version=__version__
)

{%- if cookiecutter.use_serverless == 'y' %}

handler = Mangum(app)
{%- endif %}


# TODO: Test Config!
@app.get("/info")
async def info(settings: Annotated[Base, Depends(get_settings)]):
    return {
        "scope": settings.scope,
        "database_url": settings.database_url
    }
