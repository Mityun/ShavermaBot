from aiogram.types import Message
from loader import dp, db
from handlers.user.menu import orders
from filters import IsAdmin
from utils.orders import order_to_text


@dp.message_handler(IsAdmin(), text=orders)
async def process_orders(message: Message):
    orders = db.fetchall("SELECT * FROM orders")

    if len(orders) == 0:
        await message.answer("У вас нет заказов.")
    else:
        await order_answer(message, orders)


async def order_answer(message, orders):
    res = ""

    for order in orders:
        order_str = await order_to_text(order)
        res += f"{order_str}\n\n"

    await message.answer(res)
