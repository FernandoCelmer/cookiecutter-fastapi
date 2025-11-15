"""
This module contains the main application.
"""

import uvicorn

{%- if cookiecutter.use_serverless == 'y' %}
from mangum import Mangum

{%- endif %}
from app import create_app
from app.core.settings import settings

app = create_app()

{%- if cookiecutter.use_serverless == 'y' %}
handler = Mangum(app, lifespan="off")
{%- endif %}


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=settings.is_development
    )
