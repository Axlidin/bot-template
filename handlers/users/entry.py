from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum Xush kelibsiz, {message.from_user.full_name}!\n"
                         f"Bizning online do'konimizga")


mahsulotlar = [
    {
        "id": 1,
        "name": "Mahsulot 1",
        "price": 1000
    },
    {
        "id": 2,
        "name": "Mahsulot 2",
        "price": 2000
    },
    {
        "id": 3,
        "name": "Mahsulot 3",
        "price": 3000
    }
]
