from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callbackdata import tugmalar

homeButtons = InlineKeyboardButton(text='🏠home', callback_data='home')
buttons_menu = InlineKeyboardMarkup(row_width=4)

db_list = {
    'C': 'C',
    '%': '%',
    '<=': '<=',
    '/': '/',

    '7': '7',
    '8': '8',
    '9': '9',
    '*': '*',

    '4': '4',
    '5': '5',
    '6': '6',
    '-': '-',

    '1': '1',
    '2': '2',
    '3': '3',
    '+': '+',

    '.': '.',
    '0': '0',
    '=': '='
}
for k, v in db_list.items():
    buttons_menu.insert(InlineKeyboardButton(text=k, callback_data=v))
buttons_menu.add(homeButtons)