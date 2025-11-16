"""
This module contains the item schemas.
"""

from uuid import UUID

from pydantic import BaseModel


class SchemaBase(BaseModel):
    """Base schema for the item."""

    title: str
    description: str
    status: bool = True


class SchemaPatch(BaseModel):
    """Patch schema for the item."""

    title: str | None = None
    description: str | None = None
    status: bool | None = None


class SchemaCreate(SchemaBase):
    """Create schema for the item."""


class Schema(SchemaBase):
    """Schema for the item."""

    id: UUID

    class Config:
        """Config for the item."""

        from_attributes = False
