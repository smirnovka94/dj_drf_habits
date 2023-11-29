import requests
from config.settings import TG_TOKEN, TG_NAME_ID
from habits.models import Habit
import datetime
from django.utils import timezone
from celery import shared_task

token = TG_TOKEN
user_id = TG_NAME_ID


def get_telegram_id():
    """Функция для получения ID пользователей"""
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    response = requests.get(url)
    list_users = response.json()['result']
    user_ides = []
    for user in list_users:
        user_ides.append(user["message"]['from']['id'])
    return user_ides


def send_tg(user_id, message):
    """Функция для отправки уведомлений в телеграмм бот"""
    token = TG_TOKEN
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {
        'chat_id': user_id,
        'text': message
    }
    # Отпрака сообщения
    requests.post(url, data=data)


def habit_massage(obj):
    """Функция генерации сообщения рассылки"""
    action = obj.action
    time_limit_seconds = obj.time_limit_seconds
    award = obj.award
    related_habit = obj.related_habit
    if award:
        if time_limit_seconds:
            return f"Готовся {action} в течении {time_limit_seconds}"
        else:
            return f"Готовся {action}, после чего можешь {award}"
    elif related_habit:
        if time_limit_seconds:
            return f"Готовся {action} в течении {time_limit_seconds}, после чего можешь {related_habit.name}"
        else:
            return f"Готовся {action}, после чего можешь {related_habit.name}"
    else:
        return f"Готовся {action}"


@shared_task
def mailing_telegram():
    """Основное тело программы"""
    habits = Habit.objects.filter(is_pleasant_habit=False)
    for habit in habits:
        if not habit.is_pleasant_habit:  # Если привычка без признака приятная то выполняй код
            time_begin_habit = habit.time_begin  # Дата начала привычки при регистрации
            # Диапазон времени в который текущая data_time должна попасть
            time_up = timezone.now() - datetime.timedelta(minutes=5)
            time_after = timezone.now() + datetime.timedelta(minutes=5)

            # При времени X отправляй сообщение в телегу
            if time_up <= time_begin_habit <= time_after:
                user_id = habit.id_user.telegram_id

                message = habit_massage(habit)
                send_tg(user_id, message)
            # Если дата начала привычки раньше текущей даты то обновляй дату относительно периодичности
            elif time_begin_habit < time_up:
                days = habit.time_period_day
                if days:
                    while habit.time_begin < time_up:
                        habit.time_begin = habit.time_begin + datetime.timedelta(hours=24 * days)
                        habit.save()
