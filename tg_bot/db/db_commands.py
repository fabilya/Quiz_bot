from aiogram.types.user import User
from asgiref.sync import sync_to_async

from admin_panel.telegram.models import TgUser, Question


@sync_to_async
def create_tg_user(user: User):
    """Создаёт и возвращает экземпляр пользователя TgUser"""
    tg_user = TgUser.objects.create(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        nickname=user.username
    )
    return tg_user


@sync_to_async
def get_tg_user(user_id):
    """Возвращает экземпляр требуемого пользователя по id"""
    return TgUser.objects.filter(id=user_id).first()


@sync_to_async
def create_question(user: TgUser, add_question: str, add_answer: str):
    question = Question.objects.create(
        text=add_question,
        answer_text=add_answer,
        user=user,
    )
    return question


@sync_to_async
def random_question(user: TgUser):
    """Возвращает рандомный вопрос пользователя из БД"""
    get_random_question = Question.objects.filter(user=user).order_by('?').first().text
    return get_random_question


@sync_to_async
def count_questions(user: TgUser):
    """Возвращает количество вопросов пользователя"""
    sum_questions = Question.objects.filter(user=user).count()
    return sum_questions


@sync_to_async
def check_answer(question):
    """Возвращает ответ на рандомный вопрос"""
    quest_obj = Question.objects.filter(text=question).first()
    return quest_obj.answer_text
