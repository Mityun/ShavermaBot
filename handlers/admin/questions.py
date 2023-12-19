
from handlers.user.menu import questions
from aiogram.dispatcher import FSMContext
from aiogram.utils.callback_data import CallbackData
from keyboards.default.markups import all_right_message, cancel_message, submit_markup
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.types.chat import ChatActions
from states import AnswerState
from loader import dp, db, bot
from filters import IsAdmin

question_cb = CallbackData('question', 'cid', 'action')
"""
CallbackData
"""
@dp.message_handler(IsAdmin(), text=questions)
async def process_questions(message: Message):
    """
    Handles the admin's request for processing questions.

    :param message: The message triggering the handler.
    :return: None
    """
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    questions = db.fetchall('SELECT * FROM questions')

    if len(questions) == 0:
        await message.answer('Нет вопросов.')
    else:
        for cid, question in questions:
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton(
                'Ответить', callback_data=question_cb.new(cid=cid, action='answer')))
            await message.answer(question, reply_markup=markup)

@dp.callback_query_handler(IsAdmin(), question_cb.filter(action='answer'))
async def process_answer(query: CallbackQuery, callback_data: dict, state: FSMContext):
    """
    Processes the admin's answer to a specific question.

    :param query: The callback query triggering the handler.
    :param callback_data: The callback data associated with the query.
    :param state: The finite state machine context.
    :return: None
    """
    async with state.proxy() as data:
        data['cid'] = callback_data['cid']
    await query.message.answer('Напиши ответ.', reply_markup=ReplyKeyboardRemove())
    await AnswerState.answer.set()

@dp.message_handler(IsAdmin(), state=AnswerState.answer)
async def process_submit(message: Message, state: FSMContext):
    """
    Processes the admin's submitted answer to a question.

    :param message: The message containing the submitted answer.
    :param state: The finite state machine context.
    :return: None
    """
    async with state.proxy() as data:
        data['answer'] = message.text
    await AnswerState.next()
    await message.answer('Убедитесь, что не ошиблись в ответе.', reply_markup=submit_markup())

@dp.message_handler(IsAdmin(), text=cancel_message, state=AnswerState.submit)
async def process_send_answer(message: Message, state: FSMContext):
    """
    Handles the admin's cancellation of the submitted answer.

    :param message: The message containing the cancellation request.
    :param state: The finite state machine context.
    :return: None
    """
    await message.answer('Отменено!', reply_markup=ReplyKeyboardRemove())
    await state.finish()

@dp.message_handler(IsAdmin(), text=all_right_message, state=AnswerState.submit)
async def process_send_answer(message: Message, state: FSMContext):
    """
    Processes the admin's confirmation to submit the answer.

    :param message: The message containing the confirmation.
    :param state: The finite state machine context.

    :return: None
    """
    async with state.proxy() as data:
        answer = data['answer']
        cid = data['cid']
        question = db.fetchone('SELECT question FROM questions WHERE cid=?', (cid,))[0]
        db.query('DELETE FROM questions WHERE cid=?', (cid,))
        text = f'Вопрос: <b>{question}</b>\n\nОтвет: <b>{answer}</b>'
        await message.answer('Отправлено!', reply_markup=ReplyKeyboardRemove())
        await bot.send_message(cid, text)
    await state.finish()
