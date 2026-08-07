from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.database.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(255), nullable=False)
    category = Column(String(100))
    source = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)