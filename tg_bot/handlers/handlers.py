from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


start_project_router = Router()

GREETINGS = (
    'Привет, {message.from_user.first_name}!\n'
    'Я бот, который поможет вам проверить свои знания'
)


@start_project_router.message(Command('start'))
async def command_start(message: Message, state: FSMContext):
    """Ввод команды /start"""
    await message.answer(GREETINGS.format(message=message))



