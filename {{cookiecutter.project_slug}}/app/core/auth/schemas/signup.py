from typing import Optional
from pydantic import BaseModel, EmailStr, SecretStr


class SchemaSignup(BaseModel):
    email: EmailStr
    username: Optional[str] = None
    password: SecretStr
