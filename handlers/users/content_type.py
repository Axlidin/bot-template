from aiogram import types
from loader import bot, dp
from pathlib import Path

download_path = Path().joinpath('downloads', 'category')
download_path.mkdir(parents=True, exist_ok=True)

@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer('Siz matn yubordingiz')
    # print(message.message_id)


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
# @dp.message_handler(content_types='document')
async def doc(message: types.Message):
    # print(message.document.file_id)
    await message.document.download(destination=download_path)
    await message.answer('Siz documnet yubordingiz')

@dp.message_handler(content_types=types.ContentType.VIDEO)
async def voice(message: types.Message):
    await message.video.download(destination=download_path)
    await message.answer('Siz video yubordingiz')

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def photo(message: types.Message):
    # print(message.photo[-1].file_id)
    await message.photo[-1].download(destination=download_path)
    await message.answer('Siz rasm yubordingiz')