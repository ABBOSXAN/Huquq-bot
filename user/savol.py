# from aiogram import types
# from buttons import menu_kb, kb
# from telebot import bot, dp
import wikipedia
from aiogram import types
from aiogram.utils.markdown import text
from telebot import *


# from buttons.callback_data import lang, main
# from buttons import btn_main, phone, btn_info, btn_lang
# from data import data1


# --------------- START---------------------


# ----------- CONTACT TEKSHIRISH -------

# @dp.message_handler(content_types=ContentType.CONTACT)
# async def num(message: Message):
# code = data1()['conf_code']
# await message.answer(f'Bizga tasdiqlash kodini yuboring! \n\n{code} 🔑', reply_markup=ReplyKeyboardRemove)
# await message.delete()


# --------------- DATAGA QOSHISH -----------

# @dp.message_handler(text=[data1()['conf_code'], data1()['name'], data1()['raqam']])
# async def answer(message:Message):
#     await message.delete()
#
#     if message.text == data1()['conf_code']:
#         await bot.send_message(message.from_user.id, text='Ajoyib!')
#
#     elif message.text==data1()['name']:
#         await bot.send_message(message.from_user.id, text='Ismingzni kiriting: ')
#
#     elif message.text==data1()['raqam']:
#         await bot.send_contact(message.from_user.id, phone, text='Raqamingzni kiriting: ')
#     await message.answer(text=f"{data1()['name']} ma'lumotlaringiz qabul qilindi!")


@dp.message_handler(text="Huquqiy qonun va hujjatlar")
async def handler(message: types.Message):
    text1 = """
    📄Batafsil ma'lumotlar 👇:

    https://lex.uz/docs/-5378966
        """
    await message.answer(text1)
