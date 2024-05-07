from aiogram.utils.keyboard import InlineKeyboardBuilder


def question_kb():
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Записать вопрос',
        callback_data='question',
    )
    return builder.as_markup()


def quiz():
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Записать вопрос',
        callback_data='question',
    ),
    builder.button(
        text='Викторина',
        callback_data='quiz',
    )
    return builder.as_markup()



