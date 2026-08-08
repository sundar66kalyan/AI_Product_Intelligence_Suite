import feedparser


class GoogleTrendCollector:

    def get_trending(self):

        url = "https://trends.google.com/trending/rss?geo=US"

        feed = feedparser.parse(url)

        trends = []

        for item in feed.entries:
            trends.append(item.title)

        return trends