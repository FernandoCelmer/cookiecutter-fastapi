"""
This module contains the auth endpoints.
"""

from fastapi import APIRouter, HTTPException, Depends, Security
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.core.auth.schemas.login import SchemaLogin
from app.core.auth.schemas.signup import SchemaSignup
from app.core.auth.security import security, auth_handler
from app.core.auth.models.auth_user import ControllerAuthUser
from app.core.database import Database


auth = APIRouter(tags=["Auth"])


@auth.post('/signup')
{%- if cookiecutter.use_async == 'y' %}
async def signup(
        user: SchemaSignup,
        db: Session = Depends(Database.get_db)):
{%- elif cookiecutter.use_async == 'n' %}
def signup(
        user: SchemaSignup,
        db: Session = Depends(Database.get_db)):
{%- endif %}
    query_user = ControllerAuthUser(db=db).read(params={"email": user.email})

    if query_user:
        raise HTTPException(
            status_code=422,
            detail='Account already exists'
        )

    hashed_password = auth_handler.encode_password(user.password.get_secret_value())
    query_user = ControllerAuthUser(db=db).create(
        data={
            "email": user.email,
            "username": user.username,
            "password": hashed_password})

    return SchemaSignup(**query_user.__dict__)


@auth.post('/login')
{%- if cookiecutter.use_async == 'y' %}
async def login(
        user: SchemaLogin,
        db: Session = Depends(Database.get_db)):
{%- elif cookiecutter.use_async == 'n' %}
def login(
        user: SchemaLogin,
        db: Session = Depends(Database.get_db)):
{%- endif %}
    query_user = ControllerAuthUser(db=db).read(params={"email": user.email})

    if not query_user:
        raise HTTPException(
            status_code=401,
            detail='Invalid email'
        )

    if (not auth_handler.verify_password(user.password.get_secret_value(), query_user.password)):
        raise HTTPException(
            status_code=401,
            detail='Invalid password'
        )

    access_token = auth_handler.encode_token(query_user.email)
    refresh_token = auth_handler.encode_refresh_token(query_user.email)

    return {"access_token": access_token, "refresh_token": refresh_token}


@auth.get('/refresh_token')
{%- if cookiecutter.use_async == 'y' %}
async def refresh_token(
        credentials: HTTPAuthorizationCredentials = Security(security)):
{%- elif cookiecutter.use_async == 'n' %}
def refresh_token(
        credentials: HTTPAuthorizationCredentials = Security(security)):
{%- endif %}
    refresh_token = credentials.credentials
    new_token = auth_handler.refresh_token(refresh_token)

    return {"access_token": new_token}
