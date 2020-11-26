import json

import feedparser
import requests

from settings_secret import *
from google.cloud import translate_v2 as translate

translate_client = translate.Client.from_service_account_json("credentials.json")


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
        # 翻訳
        result = translate_client.translate(text, target_language="ja")  # type: dict
        translated_text = result['translatedText']  # type: str
        print(translated_text, url)

        data = {  # type: dict
            "attachments": [
                {
                    "color": "35373B",
                    "blocks": [
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": ":devto: *DEV Community*\n{}\n{}".format(translated_text, url)
                            }
                        }
                    ]
                }
            ]
        }
        payload = json.dumps(data).encode("utf-8")  # type: json
        requests.post(POSTED_IN_URL, payload)


if __name__ == '__main__':
    fetch_rss()
