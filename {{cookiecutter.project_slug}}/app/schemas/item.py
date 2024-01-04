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
{%- if cookiecutter.id_type == 'UUID' %}
    id: UUID = Field(default_factory=uuid4)
{%- endif %}
{%- if cookiecutter.id_type == 'Integer' %}
    id: int
{%- endif %}

    class Config:
        from_attributes = False
