import feedparser


RSS_FEEDS = {
    "TechCrunch": "https://techcrunch.com/feed/",
    "OpenAI": "https://openai.com/news/rss.xml",
    "HuggingFace": "https://huggingface.co/blog/feed.xml",
    "Google AI": "https://blog.google/technology/ai/rss/",
}


class RSSCollector:

    def collect(self):

        articles = []

        for source, url in RSS_FEEDS.items():

            feed = feedparser.parse(url)

            for item in feed.entries[:5]:

                articles.append(
                    {
                        "source": source,
                        "title": item.title,
                        "link": item.link,
                    }
                )

        return articles	