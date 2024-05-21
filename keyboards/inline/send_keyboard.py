from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
otm_keys = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🧭 Joylashuvni yuborish", callback_data="mylocation"),
        InlineKeyboardButton(text="📞 Conatct yuborish", callback_data="mycontact"),
    ],
])