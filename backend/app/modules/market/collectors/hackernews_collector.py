import requests


class HackerNewsCollector:

    URL = "https://hn.algolia.com/api/v1/search?tags=front_page"

    def collect(self):

        response = requests.get(self.URL, timeout=10)

        response.raise_for_status()

        data = response.json()

        news = []

        for item in data["hits"][:15]:

            news.append(
                {
                    "title": item.get("title"),
                    "author": item.get("author"),
                    "url": item.get("url"),
                    "points": item.get("points"),
                }
            )

        return news