from app.database.base import Base
from app.database.session import engine

from app.models.product import Product
from app.models.history import History


def create_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
    print("✅ Database tables created successfully!")