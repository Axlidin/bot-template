from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
keyboard_contact = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="Contact yuboring",
                                                      request_contact=True)
                                   ],
                               ])
