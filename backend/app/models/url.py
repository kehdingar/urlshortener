from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.database.config import Base


class URL(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True)  # Add a primary key column
    full_url = Column(String, index=True)
    short_url = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)