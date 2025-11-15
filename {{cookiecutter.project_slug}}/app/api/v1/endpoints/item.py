"""
Item endpoints.
"""

from uuid import UUID

from fastapi import APIRouter, Depends

{%- if cookiecutter.use_auth == 'y' %}
from app.core.auth.security import authorization
{%- endif %}
{%- if cookiecutter.id_type == 'UUID' %}
{%- endif %}

router = APIRouter()


@router.get("", summary="Get items", response_description="List of items")
{%- if cookiecutter.use_async == 'y' %}
async def get_items({% if cookiecutter.use_auth == 'y' %}auth=Depends(authorization){% endif %}):
{%- elif cookiecutter.use_async == 'n' %}
def get_items({% if cookiecutter.use_auth == 'y' %}auth=Depends(authorization){% endif %}):
{%- endif %}
    """Get all items."""
    return {"resource": "item"}


@router.get("/{item_id}", summary="Get item by ID")
{%- if cookiecutter.use_async == 'y' %}
async def get_item(item_id: {% if cookiecutter.id_type == 'UUID' %}UUID{% elif cookiecutter.id_type == 'Integer' %}int{% endif %}{% if cookiecutter.use_auth == 'y' %}, auth=Depends(authorization){% endif %}):
{%- elif cookiecutter.use_async == 'n' %}
def get_item(item_id: {% if cookiecutter.id_type == 'UUID' %}UUID{% elif cookiecutter.id_type == 'Integer' %}int{% endif %}{% if cookiecutter.use_auth == 'y' %}, auth=Depends(authorization){% endif %}):
{%- endif %}
    """Get a specific item by ID."""
    return {"item_id": item_id, "resource": "item"}
