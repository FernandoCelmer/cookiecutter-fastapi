import uuid

from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    String,
    Uuid
)
from app.core.database import Base, engine


class Item(Base):
    """Model Item
    """

    __tablename__ = "item"
    __table_args__ = {'extend_existing': True}

    # TODO: Add options for UUID and Integer type ID
    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(75))
    description = Column(String(100))
    status = Column(Boolean, default=False)
    created_date = Column(
        DateTime,
        default=datetime.utcnow
    )
    update_date = Column(
        DateTime, 
        default=datetime.utcnow, 
        onupdate=datetime.utcnow
    )


Base.metadata.create_all(bind=engine)
