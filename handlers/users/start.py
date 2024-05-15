from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import CHANNELS
from utils.misc import subscription
from keyboards.inline.subscription import check_button
from loader import dp, bot


# @dp.message_handler(CommandStart())
@dp.message_handler(commands=['start'])
async def show_channels(message: types.Message):
    channels_format = str() #""
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        # print(invite_link)
        channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"

    await message.answer(f"Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling:\n"
                         f"{channels_format}",
                         reply_markup=check_button,
                         disable_web_page_preview=True)

@dp.callback_query_handler(text='check_subs')
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = ""
    for channel in CHANNELS:
        status = await subscription.check(
            user_id=call.from_user.id,
            channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"✅ <b>{channel.title}</b> kanaliga obuna bo'lganisz.\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"❌ <b>{channel.title}</b> kanaliga obuna bo'lmaganisz.\n"
                       f"<a href='{invite_link}'>Obuna bo'ling</a>\n\n")
    await call.message.answer(result, disable_web_page_preview=True)