from os import getenv
from pydantic_settings import BaseSettings


class Environment(BaseSettings):
    scope: str = "test"
    database_url: str = "sqlite:///./sql_app.db"
    secret_key: str = "MY_KEY"
