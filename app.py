import asyncio
import logging
import sys
from os import getenv
import config

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, WebAppInfo
from aiogram.utils.markdown import hbold

TOKEN = config.TOKEN

# Initialize the Dispatcher
dp = Dispatcher()
"""
Dispatcher's class instance 
"""


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Handles messages with the /start command
    """
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton('Make an order', web_app=WebAppInfo('https://en.wikipedia.org/wiki/Kebab'))
            ],
        ],
        resize_keyboard=True,
    )


@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Forwards the received message back to the sender
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # Handles message types that are not supported to be copied
        await message.answer("Nice try!")


async def main() -> None:
    """
    Initializes the Bot, sets the default parse mode, and starts polling events dispatching
    """
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


