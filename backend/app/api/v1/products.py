from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.product import ProductCreate, ProductResponse
from app.services.product_service import create_product, get_products

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductResponse)
def add_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    return create_product(db, product)


@router.get("/", response_model=list[ProductResponse])
def read_products(
    db: Session = Depends(get_db)
):
    return get_products(db)