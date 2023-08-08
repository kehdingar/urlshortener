from datetime import datetime
from sqlalchemy import Column, String, DateTime
from .database import Base


class URL(Base):
    __tablename__ = "urls"
    full_url = Column(String, index=True)
    short_url = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)