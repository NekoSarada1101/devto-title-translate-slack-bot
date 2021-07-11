import json
import requests
from settings import SLACK_WEBHOOK_URL
from google.cloud import translate_v2 as translate

translate_client = translate.Client()


def do_post(request):
    username = request.form.get('username')  # type: str
    image = request.form.get('image')  # type: str
    text = request.form.get('text')  # type: str
    mention = request.form.get('mention')  # type: str
    retweet = request.form.get('retweet')  # type: str
    print("username=" + username)
    print("image=" + image)
    print("text=" + text)
    print("mention=" + mention)
    print("retweet=" + retweet)

    if mention == "false" and text[0] == "@":  # メンションを除外
        return "devto"

    if retweet == "false" and text[:2] == "RT":  # リツイートを除外
        return "devto"

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

    data = {  # type: dict
        "text": "{} *{}*\n{}\n{}".format(image, username, translated_text, url),
        "unfurl_links": "true",
    }
    payload = json.dumps(data).encode("utf-8")  # type: json
    response = requests.post(SLACK_WEBHOOK_URL, payload)
    print(response)
    return "devto"
