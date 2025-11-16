"""
This module contains the FastAPI application.
"""

__version__ = "{{ cookiecutter.version }}"

__author__ = '{{ cookiecutter.author_name }} <{{ cookiecutter.email }}>'


from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
{%- if cookiecutter.use_templates == 'y' %}
from fastapi.staticfiles import StaticFiles
{%- endif %}

from app.api.v1 import api_router as v1_router
{%- if cookiecutter.use_auth == 'y' %}
from app.core.auth.endpoints import auth
{%- endif %}
{%- if cookiecutter.use_templates == 'y' %}
from app.core.templates import templates
{%- endif %}
from app.core.settings import settings

app = FastAPI(
    title="{{ cookiecutter.project_name }}",
    description="{{ cookiecutter.description }}",
    version=__version__,
    debug=settings.is_development,
)


def create_app() -> FastAPI:
    """Create the FastAPI application."""

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    {%- if cookiecutter.use_templates == 'y' %}
    # Mount static files directory
    static_dir = Path(__file__).parent / "static"
    if static_dir.exists():
        app.mount(
            "/static",
            StaticFiles(directory=str(static_dir)),
            name="static"
        )
    {%- endif %}

    {%- if cookiecutter.use_auth == 'y' %}
    app.include_router(auth, prefix="/auth")
    {%- endif %}
    app.include_router(v1_router, prefix=settings.api_v1_prefix)

    return app
