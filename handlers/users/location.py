from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.default.location_button import keyboard_location
from loader import dp, bot
from utils.get_distance import choose_shortest


@dp.callback_query_handler(text="mylocation")
async def show_location_keys(call: CallbackQuery):
    await call.message.answer(text="Joylashuvni yuborish\n<b>(joylashuvni 🧭 yoqishni unutmang):</b>",
                              reply_markup=keyboard_location)

@dp.message_handler(content_types='location')
async def get_location(message: Message):
    location = message.location
    latitude = location.latitude
    longitude = location.longitude

    closest_otm = choose_shortest(location)

    text = "\n\n".join([f"<a href='{url}'>{otm_name}</a>\n Masofa: {distance:.1f} km."
                        for otm_name, distance, url, otm_location in closest_otm])
    await message.answer(f"Rahmat. \n"
                         f"Latitude = {latitude}\n"
                         f"Longitude = {longitude}\n\n"
                         f"{text}", disable_web_page_preview=True, reply_markup=ReplyKeyboardRemove())

    for shop_name, distance, url, shop_location in closest_otm:
        await message.answer_location(latitude=shop_location["lat"],
                                      longitude=shop_location["lon"])

