from flask import Flask, request
from telegram import Bot
import keyboards

app = Flask(__name__)
TOKEN = ""
bot = Bot(TOKEN)
url = "https://xakimov.pythonanywhere.com/"

def start(user) -> None:
    # Kanal identifikatorini 'CHANNEL_ID' bilan almashtiring
     
    start_message = is_start(user)
    try:
        if start_message:
            bot.send_message(
                chat_id=user['id'],
                text=f"Assalomu aleykum {user['first_name']}. /menu comandasini bosib kalitni olishingiz mumkin!",
                reply_markup=keyboards.kalit_keyboard
            )
        else:
            bot.send_message(
                chat_id=user['id'],
                text="❌ Kechirasiz botimizdan foydalanishdan oldin ushbu kanallarga a'zo bo'lishingiz kerak. A'zo bo'lib Tasdiqlash tugmasini bosing",
                reply_markup=keyboards.replay_guruh
            )
            bot.send_message(
                chat_id=user['id'],
                text = "Kanalga qo'shilganingizni tasdiqlang.",
                reply_markup=keyboards.replay_tasqid
            )
    except:
        bot.send_message(
            chat_id=user['id'],
            text="Kechirasiz sizning so'riving tufayli serverda xatolik yuz berdi."
        )

def is_start(user: str):
    user_id = user['id']
    channel_id1 = '@CryptoLionUz'
    channel_id2 = '@UzCryptoKing'
    channel_id3 = '@DasturchiningKundaligi'
    is_subscribed1 = bot.get_chat_member(channel_id1, user_id).status != 'left'
    is_subscribed2 = bot.get_chat_member(channel_id2, user_id).status != 'left'
    is_subscribed3 = bot.get_chat_member(channel_id3, user_id).status != 'left'

    return is_subscribed1 and is_subscribed2 and is_subscribed3

def menu_page(user: str):
    if is_start(user)==False:
        start(user)
    else:
        bot.send_message(
            chat_id=user['id'],
            text = """Quyidagi tugmani bosish orqali kalitni olishingiz mumkin:👇🏻""",
            reply_markup=keyboards.kalit_keyboard
        )


@app.route('/', methods=["POST"])
def main():
    data = request.get_json()
    user = data['message']['chat']

    if data['message'].get('text')!=None :
        if data['message']['text'] == '/start' or data['message']['text']=="👉 ✅ Tasdiqlash 👈":
            start(user)
        elif data['message']['text']=="/menu" :
            if is_start(user)==False:
                start(user)
            menu_page(user)
        
    return "Hello programmer"

if __name__=="__main__":
    app.run(debug=True)
