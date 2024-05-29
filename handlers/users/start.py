from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardMarkup, LabeledPrice

from handlers.users.products_all import basket
from keyboards.default.entry_keyboards import entry_mainMenu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum Xush kelibsiz, {message.from_user.full_name}!\n"
                         f"Bizning online do'konimizga")
    await message.answer("Foydalanish uchun pastdagi tugmalardan birini tanglang",
                         reply_markup=entry_mainMenu)


productlar = ['grill', 'book', 'lavash', 'hot-Dog', 'cake']
products = {
    'grill': {
        'title': 'Grill',
        'description': 'Grillga to\'lov qilish uchun quyidagi tugmani bosing.',
        'currency': 'UZS',
        'prices': [
            LabeledPrice(
                label='Grill',
                amount=5000000,
            ),
            LabeledPrice(
                label='Yetkazib berish (7 kun)',
                amount=1000000,
            )
        ],
        'payload': 'payload:grill'
    },
    'book': {
        'title': 'Kitob',
        'description': 'Kitobga to\'lov qilish uchun quyidagi tugmani bosing.',
        'currency': 'UZS',
        'prices': [
            LabeledPrice(
                label='Kitob',
                amount=6000000,
            ),
            LabeledPrice(
                label='Yetkazib berish (7 kun)',
                amount=1000000,
            )
        ],
        'payload': 'payload:book'
    },
    'lavash': {
        'title': 'Lavash',
        'description': 'Lavashga to\'lov qilish uchun quyidagi tugmani bosing.',
        'currency': 'UZS',
        'prices': [
            LabeledPrice(
                label='Lavash',
                amount=2500000,
            ),
            LabeledPrice(
                label='Yetkazib berish (7 kun)',
                amount=1000000,
            )
        ],
        'payload': 'payload:lavash'
    },
    'hot-dog': {
        'title': 'Hot-Dog',
        'description': 'Hot-Dogga to\'lov qilish uchun quyidagi tugmani bosing.',
        'currency': 'UZS',
        'prices': [
            LabeledPrice(
                label='Hot-Dog',
                amount=1500000,
            ),
            LabeledPrice(
                label='Yetkazib berish (7 kun)',
                amount=1000000,
            )
        ],
        'payload': 'payload:hot-dog'
    }
}

@dp.message_handler(text='🛍 mahsulotlar')
async def mahsulotlar_entry(message: types.Message):
    product_mainMenu = ReplyKeyboardMarkup(resize_keyboard=True,
                                           one_time_keyboard=True,
                                           row_width=2)
    for k, v in products.items():
        # print(k)
        product_mainMenu.insert(k)
    await message.answer("Kerakli mahsulotni tanglang",
                         reply_markup=product_mainMenu)

@dp.message_handler(text='🛒 savatim')
async def savat_entry(message: types.Message):
    basket_mainMenu = ReplyKeyboardMarkup(resize_keyboard=True,
                                           one_time_keyboard=True,
                                           row_width=2)
    for k, v in basket.items():
        # print(k)
        basket_mainMenu.insert(k.upper())
    await message.answer("Kerakli mahsulotni tanglang",
                         reply_markup=basket_mainMenu)