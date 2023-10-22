from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declared_attr
import pytz

class TimestampMixin:
    @declared_attr
    def created_at(cls):
        return Column(DateTime(timezone=True), default=datetime.now(pytz.utc), nullable=False)

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime(timezone=True),
            default=datetime.now(pytz.utc),
            onupdate=datetime.now(pytz.utc),
            nullable=False,
        )
