from aiogram.fsm.state import State, StatesGroup


class Question(StatesGroup):
    get_question = State()
    get_answer = State()
    

class Answer(StatesGroup):
    get_answer = State()
    get_question = State()

