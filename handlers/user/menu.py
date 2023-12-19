from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
from loader import dp
from filters import IsAdmin, IsUser


catalog = '🛍 Каталог'
"""catalog"""
balance = '💰 Баланс'
"""balance"""
cart = '🛒 Корзина'
"""cart"""
delivery_status = '🚚 Статус заказа'
"""delivery_status"""
settings = '⚙️ Настройка каталога'
"""settings"""
orders = '🚚 Заказы'
"""orders"""
questions = '❓ Вопросы'
"""questions"""

# Handle admin menu command
@dp.message_handler(IsAdmin(), commands='menu')
async def admin_menu(message: Message):
    """
    This function handles the 'menu' command for admin users and provides a custom keyboard for admin options.

    :param message: The message object from the admin user
    """
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(settings)
    markup.add(questions, orders)
    await message.answer('Меню', reply_markup=markup)

@dp.message_handler(IsUser(), commands='menu')
async def user_menu(message: Message):
    """
    This function handles the 'menu' command for regular users and provides a custom keyboard for user options.

    :param message: The message object from the regular user
    """
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(catalog)
    markup.add(balance, cart)
    markup.add(delivery_status)

    await message.answer('Меню', reply_markup=markup)
