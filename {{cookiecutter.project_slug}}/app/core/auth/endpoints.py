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
def signup(
        user: SchemaSignup,
        db: Session = Depends(Database.get_db)):
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
            "password": hashed_password}
        )

    return SchemaSignup(**query_user.__dict__)


@auth.post('/login')
def login(
        user: SchemaLogin,
        db: Session = Depends(Database.get_db)):
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
def refresh_token(
        credentials: HTTPAuthorizationCredentials = Security(security)):
    refresh_token = credentials.credentials
    new_token = auth_handler.refresh_token(refresh_token)

    return {"access_token": new_token}
