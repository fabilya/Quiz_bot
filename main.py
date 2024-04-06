import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher(storage=MemoryStorage())


async def main() -> None:
    logging.info('Начало работы бота.')
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_description(
        'Проверяю ответы на вопросы, отвечать нужно в войс')
    await bot.set_my_short_description('По всем вопросам @fabilya')
    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
