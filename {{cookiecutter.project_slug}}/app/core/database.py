from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, registry

from app.core.settings import Settings


engine = create_engine(
    url=settings.database_url,
    connect_args={},
    pool_recycle=300,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

mapper_registry = registry()
Base = mapper_registry.generate_base()


class Database:

    @classmethod
    def _create_engine(cls):
        """Code snippet for testing."""
        settings = Settings.get_settings()

        return create_engine(
            url=settings.database_url,
            connect_args={},
            pool_recycle=300,
            pool_pre_ping=True
        )

    @classmethod
    def _session_maker(cls):
        """Code snippet for testing."""
        engine = cls._create_engine()

        return sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=engine
        )

    @classmethod
    def get_db(cls):
        """independent database session/connectionper request."""
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
