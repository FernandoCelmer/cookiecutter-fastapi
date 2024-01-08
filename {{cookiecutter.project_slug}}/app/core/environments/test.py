from pydantic_settings import BaseSettings


class Environment(BaseSettings):
    scope: str = "test"
    database_url: str = "sqlite:///./sql_test.db"
    secret_key: str = "MY_KEY"
