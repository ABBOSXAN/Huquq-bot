from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# -------------- MAIN MENU --------------
menu_kb = ReplyKeyboardMarkup([
    [
        KeyboardButton("Huquqiy yordam bo'limi 📚")
    ],
    [
        KeyboardButton("Advokatura 📝"),
        KeyboardButton("To'lov bo'limi 💵")
    ],
],
    resize_keyboard=True)

# ------------------- 2-MENU ---------------

kb = ReplyKeyboardMarkup([
    [
        KeyboardButton('Fuqarolarning huquqiy masalalari, huquq va majburiyatlari')
    ],
    [
        KeyboardButton('Huquqiy savollar berish')
    ],
    [
        KeyboardButton('Huquqiy qonun va hujjatlar')
    ],

    [
        KeyboardButton('🔙 Bosh menu')
    ],
],
    resize_keyboard=True
)
