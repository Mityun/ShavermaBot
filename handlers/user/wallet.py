
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from filters import IsUser
from .menu import balance

# test card ==> 1111 1111 1111 1026, 12/22, CVC 000

# shopId 506751

# shopArticleId 538350


@dp.message_handler(IsUser(), text=balance)
async def process_balance(message: Message, state: FSMContext):
    """function for balance check

    :param message: Message
    :param state: FSMContext
    :return: str
    """
    await message.answer('Ваш кошелек пуст! Чтобы его пополнить нужно...')
