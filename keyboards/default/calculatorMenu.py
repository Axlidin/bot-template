from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

calculatorMenu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🧮calculator")]
    ],
    resize_keyboard=True
)