from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.callback_data import CallbackData

post_callbackData = CallbackData('create_post', 'action')

post_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🆗 chop etish', callback_data=post_callbackData.new(action='post')),
            InlineKeyboardButton(text='❌ rad etish', callback_data=post_callbackData.new(action='cancel'))
        ]
    ]
)