from aiogram.utils.keyboard import InlineKeyboardBuilder

builder = InlineKeyboardBuilder()


def question_kb():
    builder.button(
        text='Записать вопрос',
        callback_data='question',
    )
    return builder.as_markup()
