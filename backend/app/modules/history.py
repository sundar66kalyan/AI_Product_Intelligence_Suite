from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func

from app.database import Base

class History(Base):

    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)

    analysis_type = Column(String)

    title = Column(String)

    opportunity_score = Column(Integer)

    risk_score = Column(Integer)

    health_score = Column(Integer)

    result_json = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())