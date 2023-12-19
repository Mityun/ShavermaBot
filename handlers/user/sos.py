from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from keyboards.default.markups import all_right_message, cancel_message, submit_markup
from aiogram.types import Message
from states import SosState
from filters import IsUser
from loader import dp, db


@dp.message_handler(commands='sos')
async def cmd_sos(message: Message):
    """Handler for the /sos command. Sets the state of SosState.question
    and sends a request to the user to describe the problem.

    :param message: Message
    :return: None
    """
    await SosState.question.set()
    await message.answer('В чем суть проблемы? Опишите как можно детальнее и администратор обязательно вам ответит.', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=SosState.question)
async def process_question(message: Message, state: FSMContext):
    """User question handler. Writes a description of the problem to the state and sends a request to the user for confirmation.

    :param message: Message
    :param state: FSMContext
    :return: None
    """
    async with state.proxy() as data:
        data['question'] = message.text

    await message.answer('Убедитесь, что все верно.', reply_markup=submit_markup())
    await SosState.next()


@dp.message_handler(lambda message: message.text not in [cancel_message, all_right_message], state=SosState.submit)
async def process_price_invalid(message: Message):
    """Handler for invalid user input. Sends a notification about invalid input.

    :param message: Message
    :return: None
    """
    await message.answer('Такого варианта не было.')


@dp.message_handler(text=cancel_message, state=SosState.submit)
async def process_cancel(message: Message, state: FSMContext):
    """Handler for canceling input. Cancels the input and ends the state.

    :param message: Message
    :param state: FSMContext
    :return: None
    """
    await message.answer('Отменено!', reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(text=all_right_message, state=SosState.submit)
async def process_submit(message: Message, state: FSMContext):
    """A handler for confirming the sending of the request. Logs a request to the database or notifies when a limit has been exceeded.

    :param message: Message
    :param state: FSMContext
    :return: None
    """
    cid = message.chat.id

    if db.fetchone('SELECT * FROM questions WHERE cid=?', (cid,)) == None:

        async with state.proxy() as data:
            db.query('INSERT INTO questions VALUES (?, ?)',
                     (cid, data['question']))

        await message.answer('Отправлено!', reply_markup=ReplyKeyboardRemove())

    else:

        await message.answer('Превышен лимит на количество задаваемых вопросов.', reply_markup=ReplyKeyboardRemove())

    await state.finish()