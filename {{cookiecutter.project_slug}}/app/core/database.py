"""
This module contains the database configuration.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import registry, sessionmaker

from app.core.settings import settings

engine = create_engine(
    url=settings.database_url,
    connect_args={},
    pool_recycle=300,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

mapper_registry = registry()
Base = mapper_registry.generate_base()


class Database:
    """Database connection and session management."""

    @classmethod
    def _create_engine(cls):
        """Create database engine for testing."""
        from app.core.settings import get_settings

        settings = get_settings()

        return create_engine(
            url=settings.database_url,
            connect_args={},
            pool_recycle=300,
            pool_pre_ping=True,
        )

    @classmethod
    def _session_maker(cls):
        """Create session maker for testing."""
        engine = cls._create_engine()

        return sessionmaker(autocommit=False, autoflush=False, bind=engine)

    @classmethod
    def get_db(cls):
        """Independent database session/connection per request."""
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
