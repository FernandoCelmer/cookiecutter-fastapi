"""
This module contains the auth security.
"""

from fastapi import Depends, HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.auth.base import BaseAuth
from app.core.auth.models.auth_user import ControllerAuthUser
from app.core.database import Database

security = HTTPBearer()
auth_handler = BaseAuth()


async def authorization(
    db: Session = Depends(Database.get_db),
    credentials: HTTPAuthorizationCredentials = Security(security),
) -> ControllerAuthUser:
    token = credentials.credentials
    payload = auth_handler.decode_token(token=token)

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return ControllerAuthUser(db=db).read(
        params={"email": payload.get("value")}
    )
