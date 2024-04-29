from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-menu"),
            KeyboardButton(text="2-menu"),
        ]
    ],
    resize_keyboard=True
)