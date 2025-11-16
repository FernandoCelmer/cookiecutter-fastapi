"""
Item endpoints.
"""

from uuid import UUID

from fastapi import APIRouter, Depends

{%- if cookiecutter.use_auth == 'y' %}
from app.core.auth.security import authorization
{%- endif %}

router = APIRouter()


@router.get("", summary="Get items", response_description="List of items")
async def get_items({%- if cookiecutter.use_auth == 'y' %}_auth=Depends(authorization){%- endif %}):
    """Get all items."""
    return {"resource": "item"}


@router.get("/{item_id}", summary="Get item by ID")
async def get_item(item_id: UUID{%- if cookiecutter.use_auth == 'y' %}, _auth=Depends(authorization){%- endif %}):
    """Get a specific item by ID."""
    return {"item_id": item_id, "resource": "item"}
