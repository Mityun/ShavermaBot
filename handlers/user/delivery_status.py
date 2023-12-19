from aiogram.types import Message
from loader import dp, db
from utils.orders import order_to_text
from .menu import delivery_status
from filters import IsUser


@dp.message_handler(IsUser(), text=delivery_status)
async def process_delivery_status(message: Message):
    orders = db.fetchall("SELECT * FROM orders WHERE cid=?", (message.chat.id,))

    if len(orders) == 0:
        await message.answer("У вас нет активных заказов.")
    else:
        await delivery_status_answer(message, orders)


async def delivery_status_answer(message, orders):
    res = ""

    for order in orders:
        res += await order_to_text(order)
        answer = [
            "<b>Заказ пока что лежит на складе.</b>",
            " уже в пути!",
            " прибыл и ждет вас на почте!",
        ]

        res += answer[0]
        res += "\n\n"

    await message.answer(res)
