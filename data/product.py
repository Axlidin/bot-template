from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.products import Product


grill = Product(
    title="Yumshoqqina jo'jalar",
    description="Mahsulot halol va pokiza ayniqsa do'mboqqina.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label='grill',
            amount=5000000, #UZS=50,000.00
        ),
        LabeledPrice(
            label='Chegirma',
            amount=-500000, #UZS-50,000.00
        ),
    ],
    start_parameter="create_invoice_grill",
    photo_url='https://dostavka-edy-v-istre.ru/wp-content/uploads/2023/04/ab42dcd7d00c435d4ea1e9de43680030.jpg',
    # photo_width=1280,
    # photo_height=564,
    # photo_size=600,
    need_email=True,
    need_name=True,
    need_phone_number=True,
)

python_book = Product(
    title="Pythonda Dasturlash Asoslari",
    description="Kitobga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label='Kitob',
            amount=6000000,#60ming
        ),
        LabeledPrice(
            label='Yetkazib berish (7 kun)',
            amount=1000000,#10ming
        ),
        LabeledPrice(
            label='Kelib olib ketish',
            amount=-500000,#50ming
        )
    ],
    start_parameter="create_invoice_python_book",
    photo_url='https://kitoblardunyosi.uz/image/cache/catalog/001-Kitoblar/003_boshqalar/006_ilmiy_ommabop/python-web-1000x1000h.jpg',
    photo_width=851,
    photo_height=1280,
    # photo_size=800,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True, # foydalanuvchi manzilini kiritishi shart
    is_flexible=True,
)

oddiy_SHIPPING = types.ShippingOption(
    id='post_oddiy',
    title="Fargo (3 kun)",
    prices=[
        LabeledPrice(
            'Maxsus quti', 500000),
        LabeledPrice(
            '3 ish kunida yetkazish', 1000000),
    ]
)
tez_SHIPPING = types.ShippingOption(
    id='post_tez',
    title='Express pochta (1 kun)',
    prices=[
        LabeledPrice(
            '1 kunda yetkazish', 1000000),
    ]
)

joyidan_olib_SHIPPING = types.ShippingOption(id='pickup',
                                       title="Do'kondan olib ketish",
                                       prices=[
                                           LabeledPrice("Yetkazib berishsiz", -1000000)
                                       ])