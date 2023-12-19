# import pytest
# from pytest_mock import mocker
# from aiogram.types import Message
# from app import cmd_start, user_mode, admin_mode

# # Mocked instances for Message
# @pytest.fixture
# def message_instance():
#     return Message()

# # Test cases
# def test_cmd_start(message_instance, mocker):
#     # Mock the necessary functions or objects
#     mock_message_answer = mocker.patch.object(message_instance, "answer")
    
#     # Call the function to be tested
#     cmd_start(message_instance)

#     # Assertions
#     mock_message_answer.assert_called_once_with(
#         """Привет! 👋

# 🤖 Я бот-магазин по продаже шаурмы.
    
# 🛍 Чтобы перейти в каталог и выбрать приглянувшиеся товары, воспользуйтесь командой /menu.

# 💰 Пополнить счет можно через Яндекс.Кассу, Сбербанк или Qiwi.

# ❓ Возникли вопросы? Не проблема! Команда /sos поможет связаться с админами, которые постараются как можно быстрее ответить.

# """,
#         reply_markup=None,
#     )

import pytest
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message
from aiogram.utils import executor
from aiogram import executor, types

import app  
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db.storage import DatabaseManager

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

Bot.set_current(bot)

# Create a simple test case
@pytest.mark.asyncio
async def test_start_command():
    message = types.Message(
        message_id=1,
        chat=types.Chat(id=123, type="private"),
        from_user=types.User(id=456, is_bot=False, username="test_user"),
        date=1234567890,
        text="/start",
    )

    # Call the handler or function you want to test from your_bot_file
    await app.cmd_start(message)

    # Make assertions here based on the expected behavior
    # For example, you can check the reply sent by the bot
    assert message.reply_text.called