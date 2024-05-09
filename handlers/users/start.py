from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.keyboards import start_menu
from filters import IsPrivate
from loader import dp


# @dp.message_handler(IsPrivate(), CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=start_menu)


@dp.message_handler(IsPrivate(), CommandStart(deep_link='kunuz'))
async def bot_start(message: types.Message):
    args = message.get_args()
    text = f"Salom {message.from_user.get_mention()}"
    text += f"Sizni {args} tavfsiya qildi..."
    await message.answer(text)
""""""
@dp.message_handler(is_forwarded=True)
async def forward_message(message: types.Message):
    await message.answer("Siz brovning xabarini yubordingiz....")