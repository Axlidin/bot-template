from aiogram import types

from keyboards.inline.calculator_inline import buttons_menu
from loader import dp, bot

value = ''
old_value = ''

@dp.message_handler(text="🧮calculator")
async def calculator_kirsh(message: types.Message):
    await message.answer("0", reply_markup=buttons_menu)

@dp.callback_query_handler()
async def hisblash(call: types.CallbackQuery):
    global value, old_value
    if call.data == "C":
        value = ''
    elif call.data == '<=':
        if value != "":
            value = value[:len(value) - 1]
    elif call.data == '=':
        try:
            value = str(eval(value))
            call.data = ''
        except:
            value = 'Xatolik'
    else:
        value += call.data

    if value != old_value:
        if value == '':
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='0', reply_markup=buttons_menu)

        else:
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=value, reply_markup=buttons_menu)
            old_value = value

    if value == 'Xatolik':
        value = ''
