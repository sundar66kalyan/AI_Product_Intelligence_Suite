from app.modules.market.collectors.google_trends import GoogleTrendCollector
from app.modules.market.collectors.rss_collector import RSSCollector

trend_collector = GoogleTrendCollector()
rss_collector = RSSCollector()


def get_google_trends():
    return trend_collector.get_trending()


def get_latest_news():
    return rss_collector.collect()	

from app.modules.market.collectors.hackernews_collector import HackerNewsCollector

hn = HackerNewsCollector()


def get_hacker_news():
    return hn.collect()