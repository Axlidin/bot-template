from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.calculatorMenu import calculatorMenu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n"
                         f"Kerakli tugmani tanlang", reply_markup=calculatorMenu)
