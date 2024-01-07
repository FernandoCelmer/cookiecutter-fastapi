
from datetime import datetime, timedelta
from passlib.context import CryptContext
from jwt import (
    encode,
    decode,
    ExpiredSignatureError,
    InvalidTokenError
)
from fastapi import HTTPException, status
from app.core.settings import Settings


class BaseAuth:

    def __init__(self, config: dict = Settings.get_settings()) -> None:
        self.crypt = CryptContext(schemes=["sha256_crypt", "des_crypt"])
        self.secret = config.secret_key

    def encode_password(self, password):
        return self.crypt.hash(password)

    def verify_password(self, password, encoded_password):
        return self.crypt.verify(password, encoded_password)

    def encode_token(self, email):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=30),
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
        try:
            payload = decode(token, self.secret, algorithms=['HS256'])
            if (payload['scope'] == 'access_token'):
                return payload

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Scope for the Token is Invalid'
            )

        except ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Token Expired'
            )

        except InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid Token'
            )

    def encode_refresh_token(self, email):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, hours=10),
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
        try:
            payload = decode(
                jwt=refresh_token,
                key=self.secret,
                algorithms=['HS256']
            )

            if (payload['scope'] == 'refresh_token'):
                email = payload['value']
                new_token = self.encode_token(email)
                return new_token

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid Scope for Token'
            )

        except ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Refresh Token Expired'
            )

        except InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid Refresh Token'
            )
