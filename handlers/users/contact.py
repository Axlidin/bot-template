from aiogram import types
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from keyboards.default.contact_keyboard import keyboard_contact
from loader import dp


@dp.callback_query_handler(text="mycontact")
async def show_contact_keys(call: CallbackQuery):
    await call.message.answer(text="Contact yuboring",
                              reply_markup=keyboard_contact)

@dp.message_handler(content_types='contact')
async def get_contact(message: types.Message):
    # await message.answer(message.contact.phone_number)
    # await message.answer(message.contact)
    await message.answer("Sizning contactingizni qabul qildik,tez orada adminlarimiz sizga aloqaga chiqishadi."
                         , reply_markup=ReplyKeyboardRemove())