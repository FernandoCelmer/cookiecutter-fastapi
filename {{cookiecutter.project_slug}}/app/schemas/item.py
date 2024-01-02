from uuid import UUID, uuid4
from datetime import date

from typing import Optional
from pydantic import BaseModel, Field


class SchemaBase(BaseModel):
    title: str
    description: str
    status: bool = True


class SchemaPatch(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: bool = None


class SchemaCreate(SchemaBase):
    pass


class Schema(SchemaBase):
    # TODO: Add options for UUID and Integer type ID
    id: UUID = Field(default_factory=uuid4)

    class Config:
        from_attributes = False
