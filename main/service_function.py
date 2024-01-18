from config.settings import TG_BOT_TOKEN, BOT_NAME, API_ID, API_HASH

from pyrogram import Client

def send_telegram_msg(tg_username, message):
    app = Client(name=BOT_NAME, bot_token=TG_BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)
    app.start()
    try:
        chat = app.get_chat(tg_username)
        chat_id = chat.id
        app.send_message(chat_id=chat_id, text=message)
    except Exception as s:
        print(s)
        return
    app.stop()

