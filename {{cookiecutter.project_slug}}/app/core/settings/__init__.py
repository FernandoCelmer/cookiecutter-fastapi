from app.core.settings.development import Settings as Development
from app.core.settings.production import Settings as Production
from app.core.settings.test import Settings as Test


__all__ = [
    'Base',
    'Development',
    'Production',
    'Test'
]


class Base:

    @staticmethod
    def development():
        return Development()

    @staticmethod
    def production():
        return Production()

    @staticmethod
    def test():
        return Test()
