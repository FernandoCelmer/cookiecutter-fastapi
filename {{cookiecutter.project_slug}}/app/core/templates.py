"""
This module contains template configuration.
"""

from pathlib import Path

from fastapi.templating import Jinja2Templates

TEMPLATES_DIR = Path("/home") / "templates"
if not TEMPLATES_DIR.exists():
    TEMPLATES_DIR = Path(__file__).parent.parent / "static" / "templates"

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
