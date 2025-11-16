"""
This module contains the login schemas.
"""

from pydantic import BaseModel, EmailStr, SecretStr


class SchemaLogin(BaseModel):
    """Schema for user login request."""

    email: EmailStr
    password: SecretStr


class SchemaLoginOutpu(BaseModel):
    """Schema for login response."""

    access_token: str
    refresh_token: str


class SchemaRefreshToken(BaseModel):
    """Schema for refresh token response."""

    access_token: str
