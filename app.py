import search
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os

app = Flask(__name__)

# Set channel_secret, channel_access_token
CHANNEL_ACCESS_TOKEN = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
CHANNEL_SECRET = os.environ['LINE_CHANNEL_SECRET']

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    # fuzzy search for team names registered in team_list in search
    team_name=""
    for team in search.team_list.keys():
        if text in search.team_list[team][1]:
            team_name = team
    if team_name:
        # reply team members
        team_member=search.team_member(team_name)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=team_member)
        )
    else:
        # reply the player's cheer song lylic
        player_lylic=search.search_player_to_lylic(text)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=player_lylic)
        )

if __name__ == "__main__":
    # for heroku setting
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)