from asyncio import sleep

from aiogram.types import Message


async def delete_message(message: Message, sleep_time: int = 600) -> None:
    """Удаляет сообщение, по умолчанию через 600 секунд"""
    await sleep(sleep_time)
    try:
        await message.delete()
    except Exception:
        return
