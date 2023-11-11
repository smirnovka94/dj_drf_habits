from django.core.management import BaseCommand

from habits.models import Habit

from users.models import User


class Command(BaseCommand):
    """
    Класс привычек.
    """

    def handle(self, *args, **kwargs):
        habits_list = [
            {
                "name": "Пробежка",
                "id_user": User.objects.get(pk=1),
                "action": "Бегать",
                "time_begin": "2023-09-09T08:00:00",
                "place": "тренжерный зал",
                "award": "Сьесть эклер",
                "time_limit": "PT10M",
            },
            {
                "name": "Залипать в Инсте",
                "id_user": User.objects.get(pk=2),
                "action": "Скролить ленту",
                "time_begin": "2023-09-09T08:10:00",
                "place": "без места",
                "time_limit": "PT2M",
                "is_public": True,
            },
        ]

        habit_for_create = []
        for habit_item in habits_list:
            habit_for_create.append(
                Habit(**habit_item)
            )


        Habit.objects.bulk_create(habit_for_create)
        print(habit_for_create)

