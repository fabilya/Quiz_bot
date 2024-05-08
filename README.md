# Quiz-bot проверяет голосвые ответы на вопросы в стиле викторины.
<img alt="" height="400" src="https://github.com/fabilya/Quiz_bot/assets/105780672/d0f6f1d1-9071-482f-8166-a305c5c0e02b" width="700"/>

## Содержание
- [Возможности бота](#возможности-бота)
- [Технологии](#используемые-технологии)
- [Инструкция по установке](#инструкции-по-установке)
- [Автор](#автор-проекта)

### Возможности бота:
- запись личных вопросов и ответов на них
- в режиме "викторина" предлагает ответить на случайный вопрос из ваших вопросов
- помогает проверять знания по личным вопросам, путём конвертации аудио сообщений в текстовые
  - сравненивает конвертированный в текст ответ с ответом из базы данных

### Используемые технологии:

- `Python`
- `Aiogram`
- `Django`
- `Openai-whisper`
- `Pytorch`
- `Ffmpeg`
- `Setuptools-rust`
- `Tiktoken`
- `Django-grappelli`
- `Thefuzz`

### Инструкции по установке

* Клонируйте репозиторий и зайдите в него в командной строке:

```GitBash
git@github.com:fabilya/Quiz_bot.git
cd quiz_bot
```


* Установите зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Для корретной работы `openai-wisper` прочитайте документацию [OPENAI-WISPER](https://github.com/openai/whisper) раздел `setup`


* Пример файла .env, который следует создать в корневой папке:
```dotenv
BOT_TOKEN=<TOKEN>
DEBUG=<development>
SECRET_KEY=<SECRET_KEY>
```

* Применение миграции в корневой папке проекта:

```Bash
python django_app.py makemigrations
python django_app.py migrate
python django_app.py collectstatic
python django_app.py createsuperuser
```

* Запуск приложения и django-админки:
```Bash
python django_app.py runserver
python bot.py
```

### Автор проекта:
[Илья Фабиянский](https://github.com/fabilya)


