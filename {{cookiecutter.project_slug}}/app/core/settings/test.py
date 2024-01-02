from os import getenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    scope: str = 'test'
    database_url: str = "sqlite:///./sql_app.db"
