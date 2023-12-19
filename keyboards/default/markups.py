"""
Module: telegram_keyboards

Description: Contains functions to generate different keyboard markups for use in Telegram bot.
"""

from aiogram.types import ReplyKeyboardMarkup

back_message = '👈 Назад'
"""  
    Back
    """
confirm_message = '✅ Подтвердить заказ'
"""  
   Order confirm
    """
all_right_message = '✅ Все верно'
"""  
    Correct 
    """
cancel_message = '🚫 Отменить'

"""  
    Cancel   

    """
def confirm_markup():
    """
        Creates a ReplyKeyboardMarkup for confirming orders.

        :return:  ReplyKeyboardMarkup: The markup for confirming orders.
        """

    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add(confirm_message)
    markup.add(back_message)

    return markup

def back_markup():
    """
        Creates a ReplyKeyboardMarkup for going back.

        :return:  ReplyKeyboardMarkup: The markup for going back.
        """
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add(back_message)

    return markup

def check_markup():
    """
        Creates a ReplyKeyboardMarkup for checking options.

        :return: ReplyKeyboardMarkup: The markup for checking options.
        """
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.row(back_message, all_right_message)

    return markup

def submit_markup():
    """
        Creates a ReplyKeyboardMarkup for submitting actions.

        :return: ReplyKeyboardMarkup: The markup for submitting actions.
        """
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.row(cancel_message, all_right_message)

    return markup