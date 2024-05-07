from aiogram.utils.keyboard import InlineKeyboardBuilder


def question_kb():
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Записать вопрос ❓',
        callback_data='question',
    )
    return builder.as_markup()


def quiz():
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Записать вопрос ❓',
        callback_data='question',
    ),
    builder.button(
        text='Викторина 🏆',
        callback_data='quiz',
    )
    return builder.as_markup()


def next_question():
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Другой вопрос ⏭',
        callback_data='quiz'
    )
    builder.button(
        text='Закончить викторину 🛑',
        callback_data='cancel'
    )
    return builder.as_markup()



