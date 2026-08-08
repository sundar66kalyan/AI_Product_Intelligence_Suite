from fastapi import APIRouter

from app.modules.product_intelligence.services.product_service import (
    analyze_product,
)

router = APIRouter(
    prefix="/product-intelligence",
    tags=["Product Intelligence"],
)


@router.get("/analyze")
def analyze(product: str):

    return {
        "status": "success",
        "product": product,
        "analysis": analyze_product(product),
    }