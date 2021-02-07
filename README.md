# devto-title-translate-slack-bot

<img width="600" src="https://user-images.githubusercontent.com/46714670/105673862-001b8200-5f2a-11eb-8e40-eb753185e780.png">

### 概要

[dev.to](https://dev.to/)
の
[公式Twitterアカウント](https://twitter.com/thepracticaldev)
がツイートしている記事タイトルを翻訳してSlackで表示する。

### 開発環境

* Python 3.8
* [Translation API](https://cloud.google.com/translate?hl=ja)
* [Cloud Functions](https://cloud.google.com/functions?hl=ja)
* [IFTTT](https://ifttt.com)

### 使用方法

1. リポジトリをクローンする。
    ```bash
    git clone https://github.com/NekoSarada1101/devto-title-translate-slack-bot.git
    ```

2. GCPでCloud Translation APIを有効にする。

3. Cloud Functionsにデプロイする。
   ```bash
   gcloud functions deploy [NAME] --region [REGION] --entry-point do_post --runtime python38 --trigger-http --allow-unauthenticated
   ```

4. デプロイ時に出力される`httpsTrigger`のURLを保存する。
   ```bash
   httpsTrigger:
     securityLevel: SECURE_OPTIONAL
     url: https://[REGION]-[PROJECT-NAME].cloudfunctions.net/[NAME] <-this
   ```

5. IFTTTでAppletsを作成する。  
   <img width="500" src="https://user-images.githubusercontent.com/46714670/107141518-81ccd000-696c-11eb-97c1-465f5a4dc4d9.png">

### ライセンス

[MIT](https://github.com/NekoSarada1101/devto-title-translate-slack-bot/blob/main/LICENSE)
