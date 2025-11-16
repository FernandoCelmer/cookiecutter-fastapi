"""
This module contains the item controller.
"""

from sqlalchemy.orm import Session

from app.core.controller import BaseController
from app.models.item import Item


class ControllerItem(BaseController):
    """Controller for the item model."""

    def __init__(self, db: Session | None = None):
        """Initialize the Item controller."""
        super().__init__(db)
        self.model_class = Item
