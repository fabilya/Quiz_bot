import asyncio
import logging
import sys

from tg_bot.loader import bot, dp

description = (
    'Проверяю ответы на вопросы.\n'
    ''
    'Ты пишешь вопрос, а после - ответ на него.\n'
    'Я случайным образом задаю тебе вопрос из твоих вопросов\n'
    'Ты отвечаешь мне на вопрос голосом\n'
    'Я слушаю и проверяю по твоему ответу!\n'
    'В конце, я тебе скажу, правильно ли ты ответил на него или нет!'
)


async def main() -> None:
    logging.info('Начало работы бота.')
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_description(description)
    await bot.set_my_short_description('По всем вопросам @fabilya')
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
