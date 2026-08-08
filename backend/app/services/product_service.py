from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate
from app.services.history_service import save_history


def create_product(db: Session, product: ProductCreate, analysis: dict = None):

    db_product = Product(
        product_name=product.product_name,
        category=product.category,
        source=product.source
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    # Save to history if analysis is provided
    if analysis:
        save_history(
            db,
            "Product",
            product.product_name,
            analysis
        )

    return db_product


def get_products(db: Session):
    return db.query(Product).all()