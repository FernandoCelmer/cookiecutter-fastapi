from fastapi import FastAPI
{%- if cookiecutter.use_serverless == 'y' %}
from mangum import Mangum
{%- endif %}

from app import __version__
from app.api.v1.routers import router


app = FastAPI(
    title="{{ cookiecutter.project_name }}",
    description="{{ cookiecutter.description }}",
    version=__version__
)

{%- if cookiecutter.use_serverless == 'y' %}

handler = Mangum(app)
{%- endif %}
