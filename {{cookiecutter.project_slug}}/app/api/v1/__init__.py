"""
API v1 router.
"""

from fastapi import APIRouter
{%- if cookiecutter.use_templates == 'y' %}

from app.api.v1.endpoints import item, templates
{%- else %}

from app.api.v1.endpoints import item
{%- endif %}

api_router = APIRouter()

api_router.include_router(item.router, tags=["Items"], prefix="/items")
{%- if cookiecutter.use_templates == 'y' %}
api_router.include_router(templates.router, tags=["Templates"])
{%- endif %}
