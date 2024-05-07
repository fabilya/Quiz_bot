import os.path

import whisper
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from admin_panel.telegram.models import TgUser
from tg_bot.db.db_commands import create_tg_user
from tg_bot.keyboards.inline import question_kb
from tg_bot.loader import bot
from tg_bot.middlewares.blocking import BlockingMiddleware

start_project_router = Router()
start_project_router.message.middleware(BlockingMiddleware())
start_project_router.callback_query.middleware(BlockingMiddleware())


GREETINGS = (
    'Привет, {message.from_user.first_name}!\n'
    '<b>Я бот, который поможет тебе проверить свои знания</b>\n'
    'Как будешь готов, жми кнопку "Записать вопрос"'
)


@start_project_router.message(Command('start'))
async def command_start(message: Message, tg_user: TgUser):
    """Ввод команды /start"""
    if not tg_user:
        await create_tg_user(
            user=message.from_user
        )
    await message.answer(GREETINGS.format(message=message),
                         reply_markup=question_kb())


@start_project_router.message(F.voice)
async def save_voice_as_mp3(message: Message):
    """
    Скачивает голосовое сообщение и сохраняет его в формате mp3.
    После преобразования аудио в текст - удаляет файл.
    """
    split_tup = os.path.splitext(message.voice.file_unique_id)
    file_name = f'{split_tup[0]}_{message.from_user.full_name}.mp3'
    await bot.download(message.voice.file_id, file_name)

    model = whisper.load_model("base")
    result = model.transcribe(file_name, fp16=False)
    await message.answer(result['text'])

    os.remove(file_name)
