# NPB 応援歌 BOT

<a href="https://liff.line.me/1645278921-kWRPP32q/?accountId=832jhkfw" target="_blank">

<div align="center">

<img src="https://user-images.githubusercontent.com/63878044/160263824-1c2eb67b-087e-48af-9d01-a0f930e85dcc.jpg" width="300px">

</div>
</a>

[日本野球機構(NPB)](https://npb.jp/)が統括している球団の応援歌を、選手名に応じて送信する LINE BOT です。<br>
非公式かつ非営利です。
<br><br>

## 使い方

- 選手名を送信すると、その選手の応援歌を返します

<div align="center">

<img src="https://user-images.githubusercontent.com/63878044/160263829-853025c9-f801-43ad-8358-813d0c7526d0.jpg" width="400px">

</div>
<br>

- 該当する選手・応援歌が複数の場合は複数返します

<div align="center">

<img src="https://user-images.githubusercontent.com/63878044/160263933-d67b3342-42fe-410e-9bb1-840ac3179d62.jpg" width="400px">

</div>

- チーム名を送信すると、Bot に登録済みの、チームに所属する選手のリストを返します。
<div align="center">

<img src="https://user-images.githubusercontent.com/63878044/160263831-55a27481-dd08-4ee0-a319-f721aab67cf0.jpg" width="400px">

</div>

## LINE アカウントの追加

以下のいずれかの方法で追加できます。

- [ここ](https://liff.line.me/1645278921-kWRPP32q/?accountId=832jhkfw)をクリック
- ID `@832jhkfw` を検索
- QR コードをスキャン

<img src="https://user-images.githubusercontent.com/63878044/159193068-6ad710e2-304d-4b55-b8e9-585722a959c6.png" alt="bot icon" width="150px" style="margin-left:60px">

## 登録チーム

NPB が統括している、以下のチームの現役・引退選手の応援歌を登録しています。<br>
詳細は、LINE Bot の登録選手一覧機能からご覧ください。

- 東京ヤクルトスワローズ
- オリックスバファローズ
- 阪神タイガース
- 千葉ロッテマリーンズ
- 読売ジャイアンツ
- 東北楽天ゴールデンイーグルス
- 広島東洋カープ
- 福岡ソフトバンクホークス
- 中日ドラゴンズ
- 北海道日本ハムファイターズ
- 横浜 DeNA ベイスターズ
- 埼玉西武ライオンズ

## 仕組み

[LINE Messaging API SDK for Python](https://github.com/line/line-bot-sdk-python)を使用しています。<br>
また、WSGI に[gunicorn](https://gunicorn.org/)を使用し、[Heroku](https://devcenter.heroku.com/) にデプロイしています。
