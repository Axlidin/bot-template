
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def build_keyboard(product):
    keys = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Xarid qilish", callback_data=f"product:{product}"),
        ],
    ])
    return keys


def build_keyboard_basket(product):
    keys = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🛒 savatga qo'shish", callback_data=f"basket:{product}"),
        ],
    ])
    return keys
