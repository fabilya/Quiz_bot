from aiogram.utils.keyboard import ReplyKeyboardBuilder


builder = ReplyKeyboardBuilder()


def main_menu(one_time_keyboard):
    for index in range(1, 11):
        builder.button(text=f"Set {index}")
        builder.adjust(2)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=one_time_keyboard)
