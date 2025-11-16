"""
This module contains the item model.
"""
from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, Column, DateTime, String

from app.core.database import Base, engine


class Item(Base):
    """Item Model"""

    __tablename__ = "item"
    __table_args__ = {"extend_existing": True}
    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True)
    title = Column(String(75))
    description = Column(String(100))
    status = Column(Boolean, default=False)
    created_date = Column(DateTime, default=datetime.utcnow)
    update_date = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


Base.metadata.create_all(bind=engine)
