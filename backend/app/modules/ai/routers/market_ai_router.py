from fastapi import APIRouter

from app.modules.ai.services.market_ai_service import generate_market_report

router = APIRouter(
    prefix="/ai",
    tags=["AI Intelligence"]
)


@router.get("/market-analysis")
def market_analysis():

    return {
        "status": "success",
        "analysis": generate_market_report()
    }