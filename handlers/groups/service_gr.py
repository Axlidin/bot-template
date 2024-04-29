import io
from aiogram import types
from aiogram.dispatcher.filters import Command
from filters import IsGroup
from filters.admin_chat import IsAdmins
from loader import dp, bot


@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def newMember(message: types.Message):
    member = ", ".join([m.get_mention(as_html=True) for m in message.new_chat_members])
    await message.reply(f"Xush kelibsiz, {member}! siz guruhdasiz")

@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def bandMember(message: types.Message):
    if message.left_chat_member.id == message.from_user.id:
        await message.reply(f"{message.left_chat_member.get_mention(as_html=True)} guruhni tark etdi.")
    elif message.from_user.id == (await bot.me).id:
        return
    else:
        await message.reply(f"{message.left_chat_member.get_mention(as_html=True)} guruhdan haydaldi.\n"
                            f"Admin: {message.from_user.get_mention(as_html=True)}")

@dp.message_handler(IsGroup(), Command('setPhoto', prefixes='!/'), IsAdmins())
async def setPhoto(message: types.Message):
    source_msg = message.reply_to_message
    # print(source_msg)
    photo = source_msg.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(photo)
    # 1-usul
    # await bot.set_chat_photo(photo=photo)
    await message.chat.set_photo(photo=input_file)

@dp.message_handler(IsGroup(), Command('set_tittle', prefixes='!/'), IsAdmins())
async def set_title(message: types.Message):
    sources_msg = message.reply_to_message
    # print(sources_msg)
    title = sources_msg.text
    # 2-usul

    await bot.set_chat_title(message.chat.id, title=title)


@dp.message_handler(IsGroup(), Command('set_description', prefixes='!/'), IsAdmins())
async def set_description(message: types.Message):
    sources_msg = message.reply_to_message
    description = sources_msg.text
    # 1-usul
    await message.chat.set_description(description=description)
    # 2-usul
    # await bot.set_chat_description(message.chat.id, description=description)
