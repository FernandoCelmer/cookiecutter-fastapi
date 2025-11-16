"""
This module contains the main application.
"""

import uvicorn

from app import create_app
from app.core.settings import settings

app = create_app()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=settings.is_development)
