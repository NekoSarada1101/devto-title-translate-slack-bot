import feedparser


def fetch_rss():
    dic = feedparser.parse(RSS_URL)  # type: dict


if __name__ == '__main__':
    fetch_rss()
