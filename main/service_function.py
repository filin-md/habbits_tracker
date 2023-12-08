import telegram

from config.settings import TG_BOT_TOKEN

def send_telegram_msg(tg_username, message):
    bot = telegram.Bot(token=TG_BOT_TOKEN)
    chat = bot.get_chat(tg_username)
    chat_id = chat.id
    bot.send_message(chat_id=chat_id, text=message)

