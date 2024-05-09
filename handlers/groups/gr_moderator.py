import asyncio
import datetime
import re
import aiogram
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

from filters import IsGroup, IsAdmins
from loader import bot, dp

# !ro|/ro (read-only) kommandalari uchun
# foydalanuvchini read-only holatiga o'tkazish handleri
@dp.message_handler(IsGroup(), Command('ro', prefixes='!/'), IsAdmins())
async def read_only(message: types.Message):
    member = message.reply_to_message.from_user
    print(member)
    member_id = member.id
    print(member_id)
    command_parse = re.compile(r'(!ro|/ro) ?(\d+)? ?([\w+\D]+)?')
    parsed = command_parse.match(message.text)
    print(parsed)
    time = parsed.group(2)
    comment = parsed.group(3)
    print(time)
    print(comment)
    if not time:
        time = 5
    """
    !ro 5 => 5minutga yoza olmaydi
    !ro 10 => 10minutga yoza olmaydi
    !ro => yoza olaydi ammo default holat berdik biz demak 5 minutga yoza olmaydi
    /ro 5 => 5minutga yoza olaydi
    /ro 10 => 10minutga yoza olaydi
    !ro 5 sabab reklama => comment xam qo'shdik
    /ro 10 haqoratlar uchun=> comment qo'shdik
    """
    # 5 minutga yoza olamslik
    # !ro | /ro  5
    # command = '!ro|/ro' time = '5' comment=[]
    # sabab bilan
    # command = '!ro|/ro' time = '5' comment=['sabab', 'bilan']
    time = int(time)

    # qachongacha yubora olmaydigon qilish
    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

    try:
        await message.chat.restrict(user_id=member_id, can_send_messages=False,
                                    until_date=until_date)
        await message.reply_to_message.delete()
    except aiogram.utils.exceptions.BadRequest as err:
        await message.answer(f"Xatolik yuzberdi! {err}")
        return

    # sabab
    await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.full_name} {time}"
                         f" minut yozish huquqidan mahrum qilindi.\n"
                         f"Sabab: <b>{comment}</b>")

    izoh = await message.reply("Xabar 5 sekunda o'chib ketadi")
    # sekun belgilanadi va delete qilinadi
    await asyncio.sleep(5)
    await message.delete()
    await izoh.delete()

#read-only dan chiqarish
@dp.message_handler(IsGroup(), Command("unro", prefixes='!/'), IsAdmins())
async def unro(message: types.Message):
    member = message.reply_to_message.from_user
    print(member)
    member_id = member.id
    user_allowed = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_change_info=False,
        can_invite_users=True,
        can_pin_messages=False,
    )

    izoh = await message.reply("Xabar 5 sekunda o'chib ketadi")
    await message.chat.restrict(user_id=member_id, permissions=user_allowed, until_date=0)
    await message.reply(f"Foydalanuvchi {member.full_name} tiklandi!")

    await asyncio.sleep(5)
    await message.delete()
    await izoh.delete()

#usersni ban ga solish
@dp.message_handler(IsGroup(), Command('ban', prefixes='!/'), IsAdmins())
async def ban(message: types.Message):
    member = message.reply_to_message.from_user
    print(member)
    member_id = member.id
    await message.chat.kick(user_id=member_id)
    await message.answer(f"Foydalanuvchi {member.full_name} guruhdan haydaldi!")
    izoh = await message.reply("Xabar 5 sekunda o'chib ketadi")

    await asyncio.sleep(5)
    await message.delete()
    await izoh.delete()

#usersni bandan chiqarish
@dp.message_handler(IsGroup(), Command('unban', prefixes='!/'), IsAdmins())
async def unban(message: types.Message):
    member = message.reply_to_message.from_user
    print(member)
    member_id = member.id
    await message.chat.unban(user_id=member_id)
    await message.answer(f"Foydalanuvchi {member.full_name} bandan chiqarildi!")
    izoh = await message.reply("Xabar 5 sekunda o'chib ketadi")

    await asyncio.sleep(5)
    await message.delete()
    await izoh.delete()