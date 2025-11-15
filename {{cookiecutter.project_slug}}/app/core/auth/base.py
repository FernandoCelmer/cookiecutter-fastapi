"""
This module contains the base auth class.
"""

from datetime import datetime, timedelta
from passlib.context import CryptContext
from jwt import (
    encode,
    decode,
    ExpiredSignatureError,
    InvalidTokenError
)
from fastapi import HTTPException, status
from app.core.settings import settings


class BaseAuth:
    """Base Auth class."""

    def __init__(self) -> None:
        """Initialize the BaseAuth class."""
        self.crypt = CryptContext(schemes=["sha256_crypt", "des_crypt"])
        self.secret = settings.secret_key

    def encode_password(self, password):
        """Encode the password."""
        return self.crypt.hash(password)

    def verify_password(self, password, encoded_password):
        """Verify the password."""
        return self.crypt.verify(password, encoded_password)

    def encode_token(self, email):
        """Encode the token."""
        # Use token expiration time from settings
        expire_minutes = settings.access_token_expire_minutes
        payload = {
            'exp': datetime.utcnow() + timedelta(minutes=expire_minutes),
            'iat': datetime.utcnow(),
            'scope': 'access_token',
            'value': email
        }

        return encode(
            payload,
            self.secret,
            algorithm='HS256'
        )

    def decode_token(self, token):
        """Decode the token."""
        try:
            payload = decode(token, self.secret, algorithms=['HS256'])
            if payload['scope'] == 'access_token':
                return payload

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Scope for the Token is Invalid'
            )

        except ExpiredSignatureError as error:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Token Expired'
            ) from error

        except InvalidTokenError as error:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid Token'
            ) from error

    def encode_refresh_token(self, email):
        """Encode the refresh token."""
        # Use refresh token expiration time from settings
        expire_hours = settings.refresh_token_expire_hours
        payload = {
            'exp': datetime.utcnow() + timedelta(hours=expire_hours),
            'iat': datetime.utcnow(),
            'scope': 'refresh_token',
            'value': email
        }

        return encode(
            payload=payload,
            key=self.secret,
            algorithm='HS256'
        )

    def refresh_token(self, refresh_token):
        """Refresh the token."""
        try:
            payload = decode(
                jwt=refresh_token,
                key=self.secret,
                algorithms=['HS256']
            )

            if payload['scope'] == 'refresh_token':
                email = payload['value']
                new_token = self.encode_token(email)
                return new_token

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid Scope for Token'
            )

        except ExpiredSignatureError as error:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Refresh Token Expired'
            ) from error

        except InvalidTokenError as error:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid Refresh Token'
            ) from error
