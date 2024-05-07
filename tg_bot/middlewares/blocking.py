from aiogram import BaseMiddleware

from tg_bot.db.db_commands import get_tg_user


class BlockingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if event.from_user.is_bot is False:
            user = await get_tg_user(event.from_user.id)
            data['tg_user'] = user
        await handler(event, data)
