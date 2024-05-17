from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from loader import bot, dp
from states.new_post import NewPost
from data.config import ADMINS, CHANNELS
from keyboards.inline.newPost_inlineKeyboard import post_keyboard, post_callbackData

@dp.message_handler(commands='new_post')
async def new_post(message: Message):
    await message.answer("Chop etish uchun yangi postni kiriting")
    await NewPost.newMessage.set()

@dp.message_handler(state=NewPost.newMessage, content_types=types.ContentType.ANY)
async def new_post_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention = message.from_user.get_mention())
    await message.answer("Postni tekshirish uchun yuborasizmi?", reply_markup=post_keyboard)
    await NewPost.confirm.set()
    # await NewPost.next()

@dp.callback_query_handler(post_callbackData.filter(action='post'), state=NewPost.confirm)
async def new_post_confirm(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get('text')
        mention = data.get('mention')
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Post adminga yuborildi.")
    await bot.send_message(chat_id=ADMINS[0], text=f"Foydalanuvchi: {mention} quyidagi postni chop etish uchun yubordi:")
    await bot.send_message(chat_id=ADMINS[0], text=text, parse_mode='HTML', reply_markup=post_keyboard)

@dp.callback_query_handler(post_callbackData.filter(action='cancel'), state=NewPost.confirm)
async def new_post_cancel(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Postni chop etish uchun yuborilmadi.")

@dp.message_handler(state=NewPost.confirm)
async def post_unknown(message: Message):
    await message.answer("Chop etish yoki rad etishni tanlashingiz shart!")
    # await message.answer("Postni tekshirish uchun yuborasizmi?", reply_markup=post_keyboard)
    # await NewPost.confirm.set()


@dp.callback_query_handler(post_callbackData.filter(action='post'), user_id=ADMINS[0])
async def let_to_print(call: CallbackQuery, state: FSMContext):
    await call.answer("Siz chop etishga ruxsat berdingiz", show_alert=True)
    target_channel = CHANNELS[0]
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=target_channel)

@dp.callback_query_handler(post_callbackData.filter(action='cancel'), user_id=ADMINS[0])
async def cancel_to_print(call: CallbackQuery, state: FSMContext):
    await call.answer("Siz chop etishga ruxsat bermadingiz", show_alert=True)
    message = await call.message.edit_reply_markup()
