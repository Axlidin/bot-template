
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

starMenu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="about me"),
            KeyboardButton(text="kurslar"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
