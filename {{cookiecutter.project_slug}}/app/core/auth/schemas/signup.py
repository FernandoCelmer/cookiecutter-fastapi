"""
This module contains the signup schemas.
"""

from pydantic import BaseModel, EmailStr, SecretStr


class SchemaSignup(BaseModel):
    """Schema for user signup request."""

    email: EmailStr
    username: str | None = None
    password: SecretStr


class SchemaSignupResponse(BaseModel):
    """Schema for signup response."""

    email: EmailStr
    username: str | None = None
