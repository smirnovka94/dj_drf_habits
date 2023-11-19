import datetime

from django.core.management import BaseCommand
from django.utils import timezone

from habits.models import Habit
import isodate

from habits.tasks import send_tg


class Command(BaseCommand):
    @staticmethod
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



    def handle(self, *args, **kwargs):
        habit = Habit.objects.get(id=8)#filter(related_habit=True)#
        # dict_habit = habit.__dict__# Вывод всех значений
        # for k, v in dict_habit.items():
        #     print(f'{k}: {v}')
        #
        # sec = habit.time_period.total_seconds()
        # if sec > 604800:
        #     print(sec)
        # print(habit)


        # habit = Habit.objects.get(id=11)#all()
        # time_begin_habit = habit.time_begin
        # time_up = timezone.now() - datetime.timedelta(minutes=65)
        # time_after = timezone.now() + datetime.timedelta(minutes=5)
        #
        # print(habit)
        # print(habit.time_begin)
        #
        # if time_up <= time_begin_habit <= time_after:
        #     user_id = habit.id_user.telegram_id
        #     message = self.habit_massage(habit)
        #     send_tg(user_id, message)
        #     print(message)
        # elif time_begin_habit < time_up:
        #     days= habit.time_period_days
        #     while habit.time_begin < time_up:
        #         habit.time_begin = habit.time_begin + datetime.timedelta(hours=24*days)
        #         habit.save()
        #     print(habit.time_begin)


        # выводим список всех привычек
        habits = Habit.objects.all()
        for habit in habits:
            if not habit.is_pleasant_habit: #Если привычка без признака приятная то выполняй код
                time_begin_habit = habit.time_begin #Дата начала привычки при регистрации
                # диапазон времени в который текащая data_time должна попасть
                time_up = timezone.now() - datetime.timedelta(minutes=5)
                time_after = timezone.now() + datetime.timedelta(minutes=5)
                print(habit)
                if time_up <= time_begin_habit <= time_after: #При времени X отправляй сообщение в телегу
                    user_id = habit.id_user.telegram_id
                    message = self.habit_massage(habit)
                    send_tg(user_id, message)
                    print(message)
                elif time_begin_habit < time_up:
                    days = habit.time_period_days
                    if days:
                        while habit.time_begin < time_up:
                            habit.time_begin = habit.time_begin + datetime.timedelta(hours=24 * days)
                            habit.save()
                        print(habit.time_begin)