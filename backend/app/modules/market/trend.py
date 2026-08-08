from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from app.database.base import Base


class MarketTrend(Base):
    __tablename__ = "market_trends"

    id = Column(Integer, primary_key=True, index=True)

    keyword = Column(String(255), nullable=False)

    source = Column(String(100), nullable=False)

    category = Column(String(100), default="General")

    summary = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)