from os import getenv
from typing import Optional
from functools import lru_cache

from app.core.environments import (
    Development,
    Production,
    Test
)


class Settings:

    @classmethod
    def _development(cls):
        return Development()

    @classmethod
    def _production(cls):
        return Production()

    @classmethod
    def _test(cls):
        return Test()

    @classmethod
    @lru_cache
    def get_settings(cls, scope: Optional[str] = None):
        if scope:
            return getattr(cls, f'_{scope}')()

        environment = getenv('SCOPE', 'test').lower()
        return getattr(cls, f'_{environment}')()
