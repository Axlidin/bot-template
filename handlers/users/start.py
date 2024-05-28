from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.entry_keyboards import entry_mainMenu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum Xush kelibsiz, {message.from_user.full_name}!\n"
                         f"Bizning online do'konimizga")
    await message.answer("Foydalanish uchun pastdagi tugmalardan birini tanglang",
                         reply_markup=entry_mainMenu)