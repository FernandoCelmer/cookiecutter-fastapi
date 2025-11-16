"""
This module contains the auth user model.
"""

from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, Column, DateTime, String

from app.core.controller import BaseController
from app.core.database import Base, engine


class AuthUser(Base):
    """Model Auth Users"""

    __tablename__ = "auth_user"
    __table_args__ = {"extend_existing": True}

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
        index=True
    )
    email = Column(String(75), unique=True)
    username = Column(String(45), unique=True)
    password = Column(String(100), unique=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    update_date = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class ControllerAuthUser(BaseController):
    """Controller for AuthUser model operations."""

    def __init__(self, db=None):
        """Initialize the AuthUser controller."""
        super().__init__(db)
        self.model_class = AuthUser


Base.metadata.create_all(bind=engine)
