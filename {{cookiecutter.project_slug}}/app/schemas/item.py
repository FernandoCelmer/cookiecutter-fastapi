"""
This module contains the item schemas.
"""

from typing import Optional
from pydantic import BaseModel
{%- if cookiecutter.id_type == 'UUID' %}
from uuid import UUID, uuid4
from pydantic import Field
{%- endif %}


class SchemaBase(BaseModel):
    """Base schema for the item."""
    title: str
    description: str
    status: bool = True


class SchemaPatch(BaseModel):
    """Patch schema for the item."""
    title: Optional[str] = None
    description: Optional[str] = None
    status: bool = None


class SchemaCreate(SchemaBase):
    """Create schema for the item."""
    pass


class Schema(SchemaBase):
    """Schema for the item."""
{%- if cookiecutter.id_type == 'UUID' %}
    id: UUID = Field(default_factory=uuid4)
{%- endif %}
{%- if cookiecutter.id_type == 'Integer' %}
    id: int
{%- endif %}

    class Config:
        """Config for the item."""
        from_attributes = False
