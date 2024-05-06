import os.path

import whisper
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from main import bot

start_project_router = Router()

GREETINGS = (
    'Привет, {message.from_user.first_name}!\n'
    'Я бот, который поможет вам проверить свои знания'
)


@start_project_router.message(Command('start'))
async def command_start(message: Message):
    """Ввод команды /start"""
    await message.answer(GREETINGS.format(message=message))


@start_project_router.message(F.voice)
async def save_voice_as_mp3(message: Message):
    """
    Downloads a voice message and saves it in mp3 format.
    After converting audio to text, deletes the file
    """
    split_tup = os.path.splitext(message.voice.file_unique_id)
    file_name = f'{split_tup[0]}_{message.from_user.full_name}.mp3'
    await bot.download(message.voice.file_id, file_name)

    model = whisper.load_model("base")
    result = model.transcribe(file_name, fp16=False)
    await message.answer(result['text'])

    os.remove(file_name)
