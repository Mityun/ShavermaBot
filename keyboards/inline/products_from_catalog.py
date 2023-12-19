from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from loader import db

product_cb = CallbackData('product', 'id', 'action')
"""  
    CallbackData
    """
def product_markup(idx='', price=0):
    """
    Creates an InlineKeyboardMarkup for adding a product to the cart.

    :param idx: The unique ID of the product.
    :type idx: str
    :param price: The price of the product.
    :type price: int

    :return: InlineKeyboardMarkup: The markup for adding a product to the cart.
    """
    global product_cb

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(f'Добавить в корзину - {price}₽', callback_data=product_cb.new(id=idx, action='add')))

    return markup
