import os.path

import whisper
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from thefuzz import fuzz

from admin_panel.telegram.models import TgUser
from tg_bot.db.db_commands import create_tg_user, create_question, \
    random_question, count_questions, check_answer
from tg_bot.keyboards.inline import question_kb, quiz
from tg_bot.loader import bot
from tg_bot.middlewares.blocking import BlockingMiddleware
from tg_bot.misc.utils import delete_message
from tg_bot.states.all_states import Question, Answer

start_project_router = Router()
start_project_router.message.middleware(BlockingMiddleware())
start_project_router.callback_query.middleware(BlockingMiddleware())

GREETINGS = (
    'Привет, {message.from_user.first_name}!\n'
    '<b>Я бот, который поможет тебе проверить свои знания</b>\n'
    'Как будешь готов, жми кнопку "Записать вопрос"'
)

GREETINGS2 = (
    'Рад снова тебя видеть, {message.from_user.first_name}!\n'
)

ACCEPT_QUESTION = (
    'Твой вопрос и ответ успешно записаны!\n'
    'Чтобы начать проверку знаний - жми "Викторина"\n'
    'Если хочешь добавить ещё вопросы - жми "Записать вопрос"!'
)

ANSWER_FOR_QUESTION = (
    'Твой вопрос: {question}\n'
    'Отвечай с помощью воиса 📢'
)


@start_project_router.message(Command('start'))
async def command_start(message: Message, state: FSMContext, tg_user: TgUser):
    """Ввод команды /start"""
    if not tg_user:
        await create_tg_user(
            user=message.from_user
        )
        await message.answer(GREETINGS.format(message=message),
                             reply_markup=question_kb())
    else:
        await message.answer(GREETINGS2.format(message=message),
                             reply_markup=quiz())
        await state.set_state(Answer.get_question)


@start_project_router.callback_query(F.data == 'question')
async def add_question(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer('Напиши свой вопрос')
    await state.set_state(Question.get_question)


@start_project_router.message(Question.get_question)
async def add_answer(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer('Отлично! Теперь введи ответ на этот вопрос!')
    await state.set_state(Question.get_answer)


@start_project_router.message(Question.get_answer)
async def bd_question(message: Message, state: FSMContext, tg_user: TgUser):
    await state.update_data(answer_text=message.text)
    context_data = await state.get_data()
    await create_question(
        add_question=context_data['text'],
        add_answer=context_data['answer_text'],
        user=tg_user
    )
    msg = await message.answer(ACCEPT_QUESTION, reply_markup=quiz())
    await state.clear()
    await delete_message(msg)
    await state.set_state(Answer.get_question)


@start_project_router.callback_query(Answer.get_question, F.data == 'quiz')
async def quiz_time(callback: CallbackQuery, state: FSMContext,
                    tg_user: TgUser):
    await callback.message.delete()
    questions = await count_questions(user=tg_user)
    if questions > 0:
        question = await random_question(user=tg_user)
        await state.update_data(get_question=question)
        await callback.message.answer(
            ANSWER_FOR_QUESTION.format(question=question))
        await state.set_state(Answer.get_answer)
    else:
        await callback.message.answer('Ты не записал ни одного вопроса!',
                                      reply_markup=question_kb())


@start_project_router.message(Answer.get_answer, F.voice)
async def save_voice_as_mp3(message: Message, state: FSMContext):
    """
    Скачивает голосовое сообщение и сохраняет его в формате mp3.
    После преобразования аудио в текст - удаляет файл.
    """
    split_tup = os.path.splitext(message.voice.file_unique_id)
    file_name = f'{split_tup[0]}_{message.from_user.full_name}.mp3'
    await bot.download(message.voice.file_id, file_name)

    model = whisper.load_model("small")
    result = model.transcribe(file_name, fp16=False, language='ru')
    await state.update_data(get_answer=result['text'])
    context_data = await state.get_data()
    get_original_answer = await check_answer(context_data['get_question'])
    if fuzz.ratio(context_data['get_answer'], get_original_answer) > 70:
        await message.answer(f'Поздравляю, ответ: <b>{result["text"]}</b> правильный!')
    else:
        await message.answer(f'Ответ {result["text"]} не правильный')
    os.remove(file_name)
