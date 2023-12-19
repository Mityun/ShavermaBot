from aiogram.types import Message
from loader import dp, db
from .menu import delivery_status
from filters import IsUser

@dp.message_handler(IsUser(), text=delivery_status)
async def process_delivery_status(message: Message):
    """
    This function is responsible for handling delivery status messages from the user.

    :param message: The message object from the user
    """
    orders = db.fetchall('SELECT * FROM orders WHERE cid=?', (message.chat.id,))

    if len(orders) == 0:
        await message.answer('У вас нет активных заказов.')
    else:
        await delivery_status_answer(message, orders)

async def delivery_status_answer(message, orders):
    """
    This function constructs and sends the delivery status response to the user.

    :param message: The message object
    :param orders: List of orders from the database
    """

    res = ''

    for order in orders:
        res += f'Заказ <b>№{order[3]}</b>'
        answer = [
            ' лежит на складе.',
            ' уже в пути!',
            ' прибыл и ждет вас на почте!'
        ]

        res += answer[0]
        res += '\n\n'
    await message.answer(res)
