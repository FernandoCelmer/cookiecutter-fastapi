from os import getenv
from pydantic_settings import BaseSettings


class Environment(BaseSettings):
    scope: str = 'production'
    database_url: str = getenv('DATABASE_URL')
    secret_key: str = getenv('SECRET_KEY')
