from django.db import models


class TgUser(models.Model):
    """Модель пользователя"""
    id = models.BigIntegerField(verbose_name='ID пользователя в telegram',
                                primary_key=True, )
    first_name = models.CharField(verbose_name='Имя в telegram',
                                  max_length=50,)
    last_name = models.CharField(verbose_name='Фамилия в telegram',
                                 max_length=100,
                                 blank=True,
                                 null=True, )
    nickname = models.CharField(verbose_name='Никнейм в telegram',
                                max_length=50,
                                blank=True,
                                null=True, )


class Question(models.Model):
    """Модель вопроса"""
    text = models.CharField(verbose_name='Текст вопроса',
                            max_length=255,
                            unique=True, )
    answer_text = models.TextField(verbose_name='Ответ вопроса', )
    user = models.ForeignKey(TgUser,
                             verbose_name='Пользователь',
                             related_name='user_questions',
                             on_delete=models.CASCADE, )
