import os
import django

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage, Redis

from tg_bot.config import BOT_TOKEN, DEBUG


def setup_django():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "admin_panel.django_settings.settings"
    )
    os.environ.update({"DJANGO_ALLOW_ASYNC_UNSAFE": "true"})
    django.setup()


def include_all_routers():
    from tg_bot.handlers import all_routers
    dp.include_routers(*all_routers)


setup_django()
bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
if DEBUG:
    storage = MemoryStorage()
else:
    storage = RedisStorage(Redis(host='redis'))
dp = Dispatcher(storage=storage)
include_all_routers()
