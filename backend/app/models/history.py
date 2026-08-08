from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from app.database.base import Base


class History(Base):

    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)

    analysis_type = Column(String(50), nullable=False)

    title = Column(String(255), nullable=False)

    analysis = Column(Text)      # <-- ADD THIS

    opportunity_score = Column(Integer, default=0)

    risk_score = Column(Integer, default=0)

    health_score = Column(Integer, default=0)

    result_json = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)