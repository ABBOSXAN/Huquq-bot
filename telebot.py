from aiogram import executor, Dispatcher, Bot, types
from buttons.keyboard import kb, menu_kb
from wikipedia import wikipedia
from user.savol import *
wikipedia.set_lang('uz')

HELP_COMMAND = """
/start - Botni ishga  tushurish
/help - Buyruqlar
"""

TOKEN_API = '5886331994:AAGepiL1iXwlYzB4s7SYEeKUol9oB4pvdE8'
bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_sticker(message.from_user.id,
                           sticker='CAACAgIAAxkBAAEJidxknl8ZOqucvBAMRu9VdSjoqCae9AACJgADHbAvMioRyDOh9yXlLwQ')
    # text = 'Tilni tanlang:\n\nВыбирайте язык:\n 👇'
    await message.answer(text=f'Sizga qanday yordam bera olaman, {message.from_user.full_name}?', reply_markup=menu_kb)
    # await message.answer(text=text, reply_markup=btn_lang)
    await message.delete()


@dp.message_handler(text='Huquqiy yordam bo\'limi 📚')
async def handler(message: types.Message):
    await message.answer(text, reply_markup=kb)
    await message.delete()


@dp.message_handler(text='🔙 Bosh menu')
async def handler(message: types.Message):
    text1 = """Bosh menu"""
    await message.answer(text1, reply_markup=menu_kb)
    await message.delete()


@dp.message_handler(text="Fuqarolarning huquqiy masalalari, huquq va majburiyatlari")
async def handler(message: types.Message):
    text1 = """
    📄Batafsil ma'lumotlar 👇:
     
    https://lex.uz/acts/-111189
    """
    await message.answer(text1)


@dp.message_handler(text='Huquqiy savollar berish')
async def handler(message: types.Message):
    text1 = """
    Savolingizni shu yerga yozing 👇:
    """
    await message.answer(text1, reply_markup='Huquqiy savollar berish')


@dp.message_handler(text='Huquqiy savollar berish')
async def savol(message: types.Message):
    try:
        savol1 = wikipedia.summary(message.text)
        await message.answer(savol1, reply_markup="Huquqiy savollar berish")
    except:
        await message.answer("Bu mavzuga oid ma'lumot topilmadi!😔")


async def on_startup(_):
    print('Bot ishga tushdi!')


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)
