from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

entry_mainMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='mahsulotlar'),
            KeyboardButton(text='savatim'),
        ],
        [
            KeyboardButton(text='buyurtmalarim'),
            KeyboardButton(text='location'),
        ]
    ], resize_keyboard=True)