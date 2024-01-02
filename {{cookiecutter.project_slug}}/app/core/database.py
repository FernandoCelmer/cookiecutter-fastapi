from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, registry
from app.core.settings import Settings


engine = create_engine(
    url=Settings().database_url,
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


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
