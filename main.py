import feedparser
from settings_secret import *


def fetch_rss():
    dic = feedparser.parse(RSS_URL)  # type: dict
    for i, entry in enumerate(dic.entries):
        text = entry.title  # type: str
        if i == 0 or "RT by @ThePracticalDev" in text:
            continue
        # text内のurlを取得
        url = text[text.find("https://dev.to/"):len(text)]  # type: str
        # 余計な部分を削除する
        text = text.replace("#DEVCommunity", "")
        text = text.replace(text[text.find("{ author"):text.rfind("}") + 1], "")
        text = text.replace(url, "")


if __name__ == '__main__':
    fetch_rss()
