"""
This module contains the auth endpoints.
"""

from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.core.auth.models.auth_user import ControllerAuthUser
from app.core.auth.schemas.login import SchemaLogin
from app.core.auth.schemas.signup import SchemaSignup, SchemaSignupResponse
from app.core.auth.security import auth_handler, security
from app.core.database import Database

auth = APIRouter(tags=["Auth"])


@auth.post("/signup")
async def signup(
    user: SchemaSignup, db: Session = Depends(Database.get_db)
) -> SchemaSignupResponse:
    query_user = ControllerAuthUser(db=db).read(params={"email": user.email})

    if query_user:
        raise HTTPException(status_code=422, detail="Account already exists")

    hashed_password = auth_handler.encode_password(
        user.password.get_secret_value()
    )
    query_user = ControllerAuthUser(db=db).create(
        data={
            "email": user.email,
            "username": user.username,
            "password": hashed_password,
        }
    )

    return SchemaSignupResponse(
        email=query_user.email, username=query_user.username
    )


@auth.post("/login")
async def login(
    user: SchemaLogin, db: Session = Depends(Database.get_db)
) -> dict[str, str]:
    query_user = ControllerAuthUser(db=db).read(params={"email": user.email})

    if not query_user:
        raise HTTPException(status_code=401, detail="Invalid email")

    if not auth_handler.verify_password(
        user.password.get_secret_value(), query_user.password
    ):
        raise HTTPException(status_code=401, detail="Invalid password")

    access_token = auth_handler.encode_token(query_user.email)
    refresh_token = auth_handler.encode_refresh_token(query_user.email)

    return {"access_token": access_token, "refresh_token": refresh_token}


@auth.get("/refresh_token")
async def refresh_token(
    credentials: HTTPAuthorizationCredentials = Security(security),
) -> dict[str, str]:
    refresh_token = credentials.credentials
    new_token = auth_handler.refresh_token(refresh_token)

    return {"access_token": new_token}
