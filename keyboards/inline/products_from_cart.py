from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

product_cb = CallbackData('product', 'id', 'action')
"""  
    CallbackData
    """
def product_markup(idx, count):
    """
    Creates an InlineKeyboardMarkup for a product with navigation buttons.

    :param idx: The unique ID of the product.
    :type idx: str
    :param count: The count of the product.
    :type count: int

    :return: InlineKeyboardMarkup: The markup for the product.
    """
    global product_cb

    markup = InlineKeyboardMarkup()
    back_btn = InlineKeyboardButton('⬅️', callback_data=product_cb.new(id=idx, action='decrease'))
    count_btn = InlineKeyboardButton(str(count), callback_data=product_cb.new(id=idx, action='count'))
    next_btn = InlineKeyboardButton('➡️', callback_data=product_cb.new(id=idx, action='increase'))
    markup.row(back_btn, count_btn, next_btn)

    return markup
