from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message, CallbackQuery

from keyboards.default.start_menu import starMenu_keyboard
from keyboards.inline.calbackdatas import book_callback, course_callback
from keyboards.inline.courses_inline import categoryMenu, coursesMenu, booksMenu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=starMenu_keyboard)


@dp.message_handler(text_contains="kurslar")
async def select_category(message: Message):
    await message.answer(f"Mahsulot tanlang", reply_markup=categoryMenu)

@dp.callback_query_handler(text="courses")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Kurs tanlang", reply_markup=coursesMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="books")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("Kitoblar", reply_markup=booksMenu)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz
    await call.message.edit_reply_markup(reply_markup=categoryMenu)
    await call.answer()

@dp.callback_query_handler(text="home")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz
    await call.message.answer('asosiy sahifa', reply_markup=starMenu_keyboard)

# CallbackData yordamid filtrlash
@dp.callback_query_handler(course_callback.filter(item_name="telegram"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    await call.message.answer(f"Siz Mukammal Telegram Bot Kursini tanladingiz.")
    await call.answer(cache_time=60)

@dp.callback_query_handler(book_callback.filter(item_name="python_book"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    await call.answer("Buyurtmangiz qabul qilindi", cache_time=60, show_alert=True)