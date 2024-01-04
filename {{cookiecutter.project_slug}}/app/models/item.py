import uuid

from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    String,
{%- if cookiecutter.id_type == 'UUID' %}
    Uuid
{%- endif %}
{%- if cookiecutter.id_type == 'Integer' %}
    Integer
{%- endif %}
)
from app.core.database import Base, engine


class Item(Base):
    """Model Item
    """

    __tablename__ = "item"
    __table_args__ = {'extend_existing': True}


{%- if cookiecutter.id_type == 'UUID' %}
    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
{%- endif %}
{%- if cookiecutter.id_type == 'Integer' %}
    id = Column(Integer, primary_key=True, index=True)
{%- endif %}
    title = Column(String(75))
    description = Column(String(100))
    status = Column(Boolean, default=False)
    created_date = Column(
        DateTime,
        default=datetime.utcnow
    )
    update_date = Column(
        DateTime, 
        default=datetime.utcnow, 
        onupdate=datetime.utcnow
    )


Base.metadata.create_all(bind=engine)
