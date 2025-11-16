"""
Template endpoints.
"""

from fastapi import APIRouter, Request
{%- if cookiecutter.use_templates == 'y' %}
from fastapi.responses import HTMLResponse

from app.core.templates import templates
{%- endif %}

router = APIRouter()


{%- if cookiecutter.use_templates == 'y' %}
@router.get(
    "/",
    response_class=HTMLResponse,
    summary="Home page",
    tags=["Templates"]
)
async def home(request: Request) -> HTMLResponse:
    """Render the home page template."""
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "project_name": "{{ cookiecutter.project_name }}",
        },
    )


{%- endif %}
