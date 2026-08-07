from app.database.base import Base
from app.database.session import engine

# Import all models here
from app.models.product import Product


def create_tables():
    Base.metadata.create_all(bind=engine)