from flask import Flask, request
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
import keyboards

app = Flask(__name__)
TOKEN = ""
bot = Bot(TOKEN)

# Define the channels
CHANNELS = [
    '@CryptoLionUz',
    '@UzCryptoKing',
    '@DasturchiningKundaligi'
]

def start(user) -> None:
    # Send a message with an inline keyboard to verify channel subscriptions

    bot.send_message(
        chat_id=user['id'],
        text="❌ Kechirasiz botimizdan foydalanishdan oldin ushbu kanallarga a'zo bo'lishingiz kerak. A'zo bo'lib Tasdiqlash tugmasini bosing",
        reply_markup=keyboards.replay_guruh
    )

def is_subscribed(user_id: str) -> bool:
    return all(
        bot.get_chat_member(channel, user_id).status != 'left'
        for channel in CHANNELS
    )

def menu_page(user: dict):
    if not is_subscribed(user['id']):
        start(user)
    else:
        bot.send_message(
            chat_id=user['id'],
            text="Quyidagi tugmani bosish orqali kalitni olishingiz mumkin:👇🏻",
            reply_markup=keyboards.kalit_keyboard
        )

@app.route('/', methods=["POST"])
def main():
    data = request.get_json()
    if 'callback_query' in data:
        query_id = data['callback_query']['id']
        user_id = data['callback_query']['from']['id']
        data = data['callback_query']['data']
        
        if data == 'verify_subscriptions':
            if is_subscribed(user_id):
                bot.answer_callback_query(query_id, text="✅ Kanalga a'zo bo'lganingiz tasdiqlandi.")
                bot.send_message(
                    chat_id=user_id,
                    text="Kanallarga a'zo bo'lganingiz uchun rahmat! Endi /menu komandasini bosing.",
                    reply_markup=keyboards.kalit_keyboard
                )
            else:
                bot.answer_callback_query(query_id, text="❌ Siz hali ham kanallarga a'zo bo'lmagansiz.")
                start({'id': user_id})
        return "ok"

    user = data['message']['chat']
    if 'text' in data['message']:
        if data['message']['text'] == '/start':
            start(user)
        elif data['message']['text'] == '/menu':
            menu_page(user)

    return "Hello programmer"

if __name__ == "__main__":
    app.run(debug=True)
