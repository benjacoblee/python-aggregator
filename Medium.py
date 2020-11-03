import feedparser


class Medium:
    def medium_programming(self):
        feed = feedparser.parse(
            "https://medium.com/feed/tag/programming").entries
        return feed

    def medium_python(self):
        feed = feed_python = feedparser.parse(
            "https://medium.com/feed/tag/python"
        ).entries
