import asyncio
import logging
import sys

from tg_bot.loader import bot, dp


async def main() -> None:
    logging.info('Начало работы бота.')
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_description(
        'Проверяю ответы на вопросы, отвечать нужно в войс')
    await bot.set_my_short_description('По всем вопросам @fabilya')
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
