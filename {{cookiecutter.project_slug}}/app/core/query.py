"""
This module contains the query data.
"""

from sqlalchemy import Boolean, Integer

from app.core.database import Base


class QueryField:
    """Represents a single query field with its value."""

    def __init__(self, field, value):
        """Initialize a query field."""
        self.field = field
        self.value = value


class QueryData:
    """Builds query fields from model class and parameters."""

    def __new__(cls, model_class: Base, params: dict) -> list[QueryField]:
        return cls.setup(model_class=model_class, params=params)

    def __init__(self, model_class: Base, params: dict) -> None:
        """Initialize query data."""
        self.model_class = model_class
        self.params = params

    @classmethod
    def load_keys(cls, model_class: Base):
        """Load all column keys from the model class."""
        return model_class.__table__.columns.keys()

    @classmethod
    def setup(cls, model_class: Base, params: dict) -> list[QueryField]:
        """Setup query fields from model and parameters."""
        query_data = []
        model_keys = cls.load_keys(model_class=model_class)

        for param in model_keys:
            if params.get(param) is not None:
                field_model = getattr(model_class, param)
                field_value = params.get(param)

                if field_value in ["null", "None"]:
                    field_value = None

                if isinstance(field_model.type, Boolean):
                    if str(field_value).lower() in ["true", "1"]:
                        field_value = True

                    if str(field_value).lower() in ["false", "0"]:
                        field_value = False

                if (
                    isinstance(field_model.type, Integer)
                    and field_value is not None
                ):
                    field_value = int(field_value)

                query_data.append(
                    QueryField(field=field_model, value=field_value)
                )

        return query_data
