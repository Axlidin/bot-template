from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🛍 Mahsulotlar"),
            KeyboardButton("🛒 Savat"),
        ],
        [
            KeyboardButton("🗳 Buyurtmalar tarixi"),
            KeyboardButton("➕ Mahsulotlar"),
        ],
        [
            KeyboardButton("➕ Superadmin"),
            KeyboardButton("➖ Superadmin"),
        ],
        [
            KeyboardButton("✍ Superadmin"),
            KeyboardButton("📨 Post yuborish"),
        ],
        [
            KeyboardButton("⚙️ Sozlamalar"),
            KeyboardButton("📊 Statistika"),
        ],
    ],resize_keyboard=True, one_time_keyboard=True
)