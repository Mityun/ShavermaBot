from aiogram.types import Message
from loader import dp, db
from handlers.user.menu import orders
from filters import IsAdmin


@dp.message_handler(IsAdmin(), text=orders)
async def process_orders(message: Message):
    """
    Handles admin requests for processing orders.

    :param message: The message triggering the handler.
    :return: None
    """
    orders = db.fetchall('SELECT * FROM orders')

    if len(orders) == 0:
        await message.answer('У вас нет заказов.')
    else:
        await order_answer(message, orders)


async def order_answer(message, orders):
    """
    Formats and sends the orders as a response.
    :param message: The message to respond to.
    :param orders: The list of orders.
    :return: None
    """
    res = ''

    for order in orders:
        res += f'Заказ <b>№{order[3]}</b>\n\n'

    await message.answer(res)
