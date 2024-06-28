from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.keyboards import admin_keyboards
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    tg_id = message.from_user.id
    datas = await db.check_tg_id(tg_id)
    if not datas:
        try:
            await db.add_userRegistration(
                firstname=message.from_user.first_name,
                username=message.from_user.username,
                telegram_id=tg_id
            )
            if tg_id == 5419118871:
                await message.answer("Xush kelkibsiz Admin!", reply_markup=admin_keyboards)
            else:
                pass
        except Exception as e:
            print(f"Error: {str(e)}")
    if tg_id == 5419118871:
        await message.answer("Xush kelkibsiz Admin!", reply_markup=admin_keyboards)
    else:
        pass

