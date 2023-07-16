# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram import types, Dispatcher
#
#
# class FSMAdmin(StatesGroup):
#     name = State()
#     last_name = State()
#     adres = State()
#     phone = State()
#
#
# async def name(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['name'] = message.text
#     await message.reply('Ismingizni kiriting: ')
#     await FSMAdmin.next()
#     await message.reply('Familiyangizni kiriting: ')
#
#
# async def last_name(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['last_name'] = message.text
#     await FSMAdmin.next()
#     await message.reply('Manzilingizni kiriting: ')
#
#
# async def adres(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['manzil'] = message.text
#     await FSMAdmin.next()
#     await message.reply('Raqamingizni kiriting: ')
#
#
# async def phone(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['phone'] = message.text
#     await FSMAdmin.next()
#     await message.reply('Rahmat!')
#
#     async with state.proxy() as data:
#         await message.reply(str(data))
#     await state.finish()
#
# def register_handlers_admin(dp: Dispatcher):
#     dp.register_message_handler(name, state=FSMAdmin.name)
#     dp.register_message_handler(last_name, state=FSMAdmin.last_name)
#     dp.register_message_handler(adres, state=FSMAdmin.adres)
#     dp.register_message_handler(phone, state=FSMAdmin.phone)
