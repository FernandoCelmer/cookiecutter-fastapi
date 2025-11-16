"""
Settings configuration for the FastAPI application.
"""

from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    scope: Literal["development", "production", "test"] = Field(
        default="development", description="Application environment scope"
    )

    database_url: str = Field(
        default="sqlite:///./sql_app.db", description="Database connection URL"
    )

    secret_key: str = Field(
        default="dev-key-change-in-production-min-32-characters",
        description="Secret key for JWT tokens and encryption",
        min_length=32,
    )

    api_v1_prefix: str = Field(default="/api/v1", description="API v1 prefix")

    cors_origins: list[str] = Field(
        default=["*"], description="Allowed CORS origins"
    )
    access_token_expire_minutes: int = Field(
        default=30, description="Access token expiration time in minutes"
    )

    refresh_token_expire_hours: int = Field(
        default=10, description="Refresh token expiration time in hours"
    )

    @property
    def is_development(self) -> bool:
        """Check if running in development environment."""
        return self.scope == "development"


@lru_cache
def get_settings() -> Settings:
    """
    Get cached settings instance.
    This function uses lru_cache to ensure only one instance is created.
    """
    return Settings()


settings = get_settings()
