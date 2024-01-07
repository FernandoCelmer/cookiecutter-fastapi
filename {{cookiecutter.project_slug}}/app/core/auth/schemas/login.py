from pydantic import BaseModel, EmailStr, SecretStr


class SchemaLogin(BaseModel):
    email: EmailStr
    password: SecretStr


class SchemaLoginOutpu(BaseModel):
    access_token: str
    refresh_token: str


class SchemaRefreshToken(BaseModel):
    access_token: str
