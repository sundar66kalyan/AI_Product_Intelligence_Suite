from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.database.base import Base


class MarketTrend(Base):
    __tablename__ = "market_trends"

    id = Column(Integer, primary_key=True, index=True)

    keyword = Column(String(255), nullable=False)

    source = Column(String(100))

    summary = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)