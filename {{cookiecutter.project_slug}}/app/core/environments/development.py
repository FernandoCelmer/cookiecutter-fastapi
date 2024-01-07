from os import getenv
from pydantic_settings import BaseSettings


class Environment(BaseSettings):
    scope: str = 'development'
    database_url: str = getenv("DATABASE_URL", "sqlite:///./sql_app.db")
    secret_key: str = getenv('SECRET_KEY')
