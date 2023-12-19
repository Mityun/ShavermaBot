import os
import handlers
from aiogram import executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from loader import dp, db, bot
import filters
import logging

# filters.setup(dp)

WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = int(os.environ.get("PORT", 5000))
user_message = "Пользователь"
admin_message = "Админ"


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    await message.answer(
        """Привет! 👋

🤖 Я бот-магазин по подаже шаурмы.
    
🛍 Чтобы перейти в каталог и выбрать приглянувшиеся товары возпользуйтесь командой /menu.

💰 Пополнить счет можно через Яндекс.кассу, Сбербанк или Qiwi.

❓ Возникли вопросы? Не проблема! Команда /sos поможет связаться с админами, которые постараются как можно быстрее откликнуться.

    """,
        reply_markup=markup,
    )


@dp.message_handler(text=user_message)
async def user_mode(message: types.Message):
    cid = message.chat.id
    await message.answer(
        "Включен пользовательский режим.", reply_markup=ReplyKeyboardRemove()
    )


@dp.message_handler(text=admin_message)
async def admin_mode(message: types.Message):
    cid = message.chat.id

    await message.answer("Включен админский режим.", reply_markup=ReplyKeyboardRemove())


async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)
    db.create_tables()


async def on_shutdown():
    logging.warning("Shutting down..")
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning("Bot down")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
