from app.modules.market.services.trend_service import (
    get_google_trends,
    get_latest_news,
    get_hacker_news,
)


def get_market_snapshot():

    return {
        "google_trends": get_google_trends(),
        "rss_news": get_latest_news(),
        "hacker_news": get_hacker_news(),
    }