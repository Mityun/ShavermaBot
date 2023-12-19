

import logging
from aiogram.types import Message, CallbackQuery
from keyboards.inline.categories import categories_markup, category_cb
from keyboards.inline.products_from_catalog import product_markup, product_cb
from aiogram.utils.callback_data import CallbackData
from aiogram.types.chat import ChatActions
from loader import dp, db, bot
from .menu import catalog
from filters import IsUser


@dp.message_handler(IsUser(), text=catalog)
async def process_catalog(message: Message):

    """
    Обработчик запроса на просмотр каталога товаров.
    Входные данные:
        message: Message - объект сообщения
    """
    await message.answer('Выберите раздел, чтобы вывести список товаров:', reply_markup=categories_markup())


@dp.callback_query_handler(IsUser(), category_cb.filter(action='view'))
async def category_callback_handler(query: CallbackQuery, callback_data: dict):
    """
        :param query: CallbackQuery - объект колбэка
        :param callback_data: dict - параметры колбэка
        :rtype TypeError: ошибка типа данных
        :rtype KeyError: ошибка ключа
        :return none
    """

    products = db.fetchall('''SELECT * FROM products product
    WHERE product.tag = (SELECT title FROM categories WHERE idx=?) 
    AND product.idx NOT IN (SELECT idx FROM cart WHERE cid = ?)''',
                           (callback_data['id'], query.message.chat.id))
    await query.answer('Все доступные товары.')
    await show_products(query.message, products)


@dp.callback_query_handler(IsUser(), product_cb.filter(action='add'))
async def add_product_callback_handler(query: CallbackQuery, callback_data: dict):
    """
    Обработчик добавления товара в корзину.
    Входные данные:
        query: CallbackQuery - объект колбэка
        callback_data: dict - параметры колбэка
    Возможные ошибки:
        TypeError - ошибка типа данных

    Возвращаемые данные:
        Отсутствуют
    """
    db.query('INSERT INTO cart VALUES (?, ?, 1)', (query.message.chat.id, callback_data['id']))
    await query.answer('Товар добавлен в корзину!')
    await query.message.delete()


async def show_products(m, products):
    """
    Функция для отображения списка товаров.
    Входные данные:
        m: Message - объект сообщения
        products: list - список продуктов
    Возможные ошибки:
        TypeError - ошибка типа данных
    Возвращаемые данные:
        Отсутствуют
    """
    if len(products) == 0:
        await m.answer('Здесь ничего нет 😢')
    else:
        await bot.send_chat_action(m.chat.id, ChatActions.TYPING)
        for idx, title, body, image, price, _ in products:
            markup = product_markup(idx, price)
            text = f'<b>{title}</b>nn{body}'
            await m.answer_photo(photo=image, caption=text, reply_markup=markup)          reply_markup=markup)