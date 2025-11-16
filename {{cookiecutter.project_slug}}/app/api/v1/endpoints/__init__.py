"""
API v1 endpoints.
"""

from app.api.v1.endpoints import item
{%- if cookiecutter.use_templates == 'y' %}
from app.api.v1.endpoints import templates
{%- endif %}

__all__ = [
    "item"{%- if cookiecutter.use_templates == 'y' %},
    "templates"{%- endif %}
]
