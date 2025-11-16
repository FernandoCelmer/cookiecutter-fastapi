"""
Configuration for pytest tests.
"""
# flake8: noqa
# ruff: noqa
# type: ignore

import os
from pathlib import Path

import pytest
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient
{%- if cookiecutter.use_templates == 'y' %}
from fastapi.staticfiles import StaticFiles
{%- endif %}
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.api.v1 import api_router as v1_router
{%- if cookiecutter.use_auth == 'y' %}
from app.core.auth.endpoints import auth
{%- endif %}
from app.core.database import Base, Database
from app.core.settings import settings

os.environ["SCOPE"] = "test"
os.environ["DATABASE_URL"] = "sqlite:///:memory:"
os.environ["SECRET_KEY"] = (
    "test-secret-key-for-testing-only-min-32-chars"
)


@pytest.fixture(scope="function")
def db_session():
    """Create a fresh database session for each test."""
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    TestingSessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )

    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    """Create a test client with database override."""

    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    test_app = FastAPI(
        title="{{ cookiecutter.project_name }}",
        description="{{ cookiecutter.description }}",
        version="{{ cookiecutter.version }}",
        debug=settings.is_development,
    )

    test_app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    {%- if cookiecutter.use_templates == 'y' %}
    static_dir = Path(__file__).parent.parent / "app" / "static"
    if static_dir.exists():
        test_app.mount(
            "/static",
            StaticFiles(directory=str(static_dir)),
            name="static",
        )
    {%- endif %}
    {%- if cookiecutter.use_auth == 'y' %}
    test_app.include_router(auth, prefix="/auth")
    {%- endif %}
    test_app.include_router(v1_router, prefix=settings.api_v1_prefix)
    test_app.dependency_overrides[Database.get_db] = override_get_db

    with TestClient(test_app) as test_client:
        yield test_client

    test_app.dependency_overrides.clear()


{%- if cookiecutter.use_auth == 'y' %}
@pytest.fixture
def test_user_data():
    """Sample user data for testing."""
    return {
        "email": "test@example.com",
        "username": "testuser",
        "password": "testpassword123",
    }


@pytest.fixture
def test_user(client, test_user_data):
    """Create a test user."""
    response = client.post("/auth/signup", json=test_user_data)
    assert response.status_code == 200
    return response.json()


@pytest.fixture
def auth_headers(client, test_user):
    """Get authentication headers for authenticated requests."""
    response = client.post(
        "/auth/login",
        json={
            "email": test_user["email"],
            "password": "testpassword123",
        },
    )
    assert response.status_code == 200
    tokens = response.json()
    return {"Authorization": f"Bearer {tokens['access_token']}"}


@pytest.fixture
def refresh_token(client, test_user):
    """Get refresh token for testing."""
    response = client.post(
        "/auth/login",
        json={
            "email": test_user["email"],
            "password": "testpassword123",
        },
    )
    assert response.status_code == 200
    return response.json()["refresh_token"]
{%- endif %}
