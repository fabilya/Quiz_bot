import uuid

from aiogram import Router
from aiogram.types import Message, UserProfilePhotos, FSInputFile

from main import bot, dp

router = Router()


@dp.message()
async def echo_handler(message: Message) -> None:
    user_profile_photo: UserProfilePhotos = await bot.get_user_profile_photos(
        message.from_user.id)
    if user_profile_photo.total_count > 0:
        file = await bot.get_file(user_profile_photo.photos[0][2].file_id)
        filename = uuid.uuid4().hex
        await bot.download_file(file.file_path, f'{filename}.jpg')
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=FSInputFile(f'{filename}.jpg')
        )
    else:
        print('У пользователя нет фото в профиле.')

