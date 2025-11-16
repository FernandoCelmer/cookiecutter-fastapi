"""
This module contains template configuration.
"""

from pathlib import Path

from fastapi.templating import Jinja2Templates

# Path to templates directory
TEMPLATES_DIR = Path(__file__).parent.parent / "static" / "templates"

# Initialize Jinja2 templates
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

