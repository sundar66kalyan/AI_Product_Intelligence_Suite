from fastapi import APIRouter

from app.modules.market.services.trend_service import get_google_trends

router = APIRouter(
    prefix="/market",
    tags=["Market Intelligence"]
)

from app.modules.market.services.trend_service import (
    get_google_trends,
    get_latest_news,
)

@router.get("/google-trends")
def google_trends():

    return {
        "status": "success",
        "trends": get_google_trends()
    }

@router.get("/news")
def latest_news():

    return {
        "status": "success",
        "articles": get_latest_news()
    }

from app.modules.market.services.trend_service import (
    get_google_trends,
    get_latest_news,
    get_hacker_news,
)

@router.get("/hacker-news")
def hacker_news():

    return {
        "status": "success",
        "articles": get_hacker_news()
    }

from app.modules.market.services.aggregator_service import get_market_snapshot

@router.get("/snapshot")
def market_snapshot():

    return {
        "status": "success",
        "data": get_market_snapshot()
    }