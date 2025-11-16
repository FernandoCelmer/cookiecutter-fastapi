"""
This module contains template configuration.
"""

from pathlib import Path

from fastapi.templating import Jinja2Templates

TEMPLATES_DIR = Path("/home") / "templates"

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
