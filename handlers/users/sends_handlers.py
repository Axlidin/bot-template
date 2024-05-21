from aiogram import types
from aiogram.types import InputFile

from keyboards.inline.send_keyboard import otm_keys
from loader import dp


@dp.message_handler(content_types='photo')
async def get_photo(message: types.Message):
    print(message.photo[-1].file_id)

@dp.message_handler(content_types='video')
async def get_video(message: types.Message):
    print(message.video.file_id)

@dp.message_handler(commands='kitoblarim')
async def kitoblarim(message: types.Message):
    photo_id = 'AgACAgIAAxkBAAIJ5WZMtqWP2dmxWgABCe1a9m92oIlzLgACxeYxGyXQaEpyGivZe3nP0QEAAwIAA20AAzUE'
    photo_url = 'https://1.bp.blogspot.com/-_gie8qAwZPY/X0HgTfDEoMI/AAAAAAAAIjk/KsZvNYbtGHU6Dq9wi7koZ-QYfSLa8MgYwCLcBGAsYHQ/s1600/touchmaster_1598152338675.jpeg'
    photo_input = InputFile('photos/python.jpg')
    await message.reply_photo(photo=photo_id, caption="Kitoblarim")
    await message.answer_photo(photo=photo_url, caption="Kitoblarim")
    await message.answer_photo(photo=photo_input, caption="Kitoblarim")


@dp.message_handler(commands='kurslarim')
async def kurslarim(message: types.Message):
    album = types.MediaGroup()
    photo1 = 'AgACAgIAAxkBAAIJ5WZMtqWP2dmxWgABCe1a9m92oIlzLgACxeYxGyXQaEpyGivZe3nP0QEAAwIAA20AAzUE'
    photo2 = 'https://1.bp.blogspot.com/-_gie8qAwZPY/X0HgTfDEoMI/AAAAAAAAIjk/KsZvNYbtGHU6Dq9wi7koZ-QYfSLa8MgYwCLcBGAsYHQ/s1600/touchmaster_1598152338675.jpeg'
    photo3 = InputFile('photos/python.jpg')
    video1 = 'BAACAgIAAxkBAAIJ82ZMuEz-SAw2TJD31D8UUJDElO-jAALLUQACJdBoSrY8vpb-JE_iNQQ'
    album.attach_photo(photo1)
    album.attach_photo(photo2)
    album.attach_photo(photo3)
    album.attach_video(video1, caption='Bizning kurslarimiz haqida')
    await message.answer_media_group(media=album)


@dp.message_handler(commands='adu')
async def adu(message: types.Message):
    photo_id = 'AgACAgIAAxkBAAIJ-2ZMy2oWa3tm18RnwELCzThp8boJAAKI5zEbJdBoShVTeUX4fSwoAQADAgADeQADNQQ'
    await message.answer_photo(photo=photo_id,
                               caption="Siz o'zingiz uchun yaqin bo'lgan joyni aniqlashingiz mumkin", reply_markup=otm_keys)