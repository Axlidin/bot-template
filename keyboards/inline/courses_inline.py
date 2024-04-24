from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.calbackdatas import course_callback, book_callback

# 1-usul.
categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="💻 Kurslar", callback_data="courses"),
        InlineKeyboardButton(text="📚 Kitoblar", callback_data="books"),
    ],
    [
        InlineKeyboardButton(text="🔗 Mohirdev sahifasiga o'tish", url="https://mohirdev.uz/courses/telegram"),
    ],
    [
        InlineKeyboardButton(text="🔍 Qidirish", switch_inline_query_current_chat=""),
    ],
    [
        InlineKeyboardButton(text="✉️Ulashish", switch_inline_query="Zo'r bot ekan"),
    ],
    [

        InlineKeyboardButton(text="🔙 home", callback_data="home")
    ]
])


# 2-usul
coursesMenu = InlineKeyboardMarkup(row_width=1)

python = InlineKeyboardButton(text="🐍 Python Dasturlash Asoslari", callback_data=course_callback.new(item_name="python"))
coursesMenu.insert(python)

psql = InlineKeyboardButton(text="🔰 Postgresql ma'lumotlar ombori", callback_data=course_callback.new(item_name="psql"))
coursesMenu.insert(psql)

telegram = InlineKeyboardButton(text="🤖 Mukammal Telegram bot", callback_data="course:telegram")
coursesMenu.insert(telegram)

git = InlineKeyboardButton(text="Git va GitHub", callback_data="course:git")
coursesMenu.insert(git)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancel")
coursesMenu.insert(back_button)

# 3 - usul

books = {
    "Python. Dasturlash asoslari": "python_book",
    "C++. Dasturlash tili": "cpp_book",
    "Mukammal Dasturlash. JavaScript": "js_book",
}

booksMenu = InlineKeyboardMarkup(row_width=1)
for key, value in books.items():
    booksMenu.insert(InlineKeyboardButton(text=key, callback_data=book_callback.new(item_name=value)))
booksMenu.insert(back_button)