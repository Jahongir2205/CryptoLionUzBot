from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


replay_guruh = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="CryptoLionUz", url="https://t.me/CryptoLionUz")],
    [InlineKeyboardButton(text="UzCryptoKing", url="https://t.me/UzCryptoKing")],
    [InlineKeyboardButton(text="Dasturchining Kundaligi", url="https://t.me/DasturchiningKundaligi")],
    [InlineKeyboardButton("Tasdiqlash", callback_data='verify_subscriptions')]
    ])

replay_tasqid = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="👉 ✅ Tasdiqlash 👈")]
    ],
    resize_keyboard=True
)
kalit_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("Kalitni olish", url="http://t.me/CryptoLionUzBot/HamsterKeys")]
    ])
