import json
import requests
from settings import *
from google.cloud import translate_v2 as translate

translate_client = translate.Client()


def do_post(request):
    text = request.form.get('text')  # type: str
    username = request.form.get('username')  # type: str

    print("text={}, username={}".format(text, username))

    if "RT" in text or "@" in text:
        return

    # text内のurlを取得
    url = text[text.find("https://t.co/"):len(text)]  # type: str
    # 余計な部分を削除する
    text = text.replace("#DEVCommunity", "")
    text = text.replace(text[text.find("{ author"):text.rfind("}") + 1], "")
    text = text.replace(url, "")

    # 翻訳
    result = translate_client.translate(text, target_language="ja")
    translated_text = result['translatedText']  # type: str
    print(translated_text)

    icon_name = ":devto:"

    data = {  # type: dict
        "text": "{} *{}*\n{}\n{}".format(icon_name, username, translated_text, url),
        "unfurl_links": "true",
    }
    payload = json.dumps(data).encode("utf-8")  # type: json
    response = requests.post(SLACK_WEBHOOK_URL, payload)
    print(response)
    return response
