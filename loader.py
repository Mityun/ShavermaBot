"""loader of necessary configs + link to temporary data

"""
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db.storage import DatabaseManager

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
""" creating a bot instance

:param token: config.BOT_TOKEN
:param token: types.ParseMode.HTML
"""


storage = MemoryStorage()
""" storage 
"""
dp = Dispatcher(bot, storage=storage)
"""dispatcher instance
"""
db = DatabaseManager('data/database.db')
"""db instance + temporary path
"""
