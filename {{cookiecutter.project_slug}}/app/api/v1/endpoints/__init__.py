"""
API v1 endpoints.
"""

{%- if cookiecutter.use_templates == 'y' %}
from app.api.v1.endpoints import item, templates
{%- else %}
from app.api.v1.endpoints import item
{%- endif %}

__all__ = [
    "item"{%- if cookiecutter.use_templates == 'y' %},
    "templates"{%- endif %},
]
