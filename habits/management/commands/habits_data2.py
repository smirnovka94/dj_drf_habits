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
                "name": "Читать книгу",
                "id_user": User.objects.get(pk=1),
                "action": "Читать книгу",
                "time_begin": "2023-09-09 18:00:00",
                "place": "дома",
                "related_habit": Habit.objects.get(pk=2),
                "time_limit": "PT60M",
                "time_period": "PT48H"
            },

            {            {
                "name": "Просмотреть урок",
                "id_user": User.objects.get(pk=1),
                "action": "Изучить урок",
                "time_begin": "2023-09-09 18:00:00",
                "place": "в любом месте",
                "related_habit": Habit.objects.get(pk=3),
                "time_limit": "PT90M",
                "time_period": "PT48H"
            },
            {
                "name": "Глажка белья ",
                "id_user": User.objects.get(pk=1),
                "action": "Гладить одежду",
                "time_begin": "2023-09-09 18:00:00",
                "place": "дома",
                "related_habit": Habit.objects.get(pk=5),
                "time_limit": "PT60M",
                "time_period": "PT72H"
            },
            {
                "name": "Генеральная уборка",
                "id_user": User.objects.get(pk=1),
                "action": "Убирать квартиру",
                "time_begin": "2023-09-09 10:00:00",
                "place": "дома",
                "related_habit": Habit.objects.get(pk=4),
                "time_limit": "PT30M",
                "time_period": "PT168H"
            },
            {
                "name": "Стирка белья",
                "id_user": User.objects.get(pk=1),
                "action": "Стирка",
                "time_begin": "2023-09-09 18:00:00",
                "place": "дома",
                "related_habit": Habit.objects.get(pk=3),
                "time_limit": "PT20M",
                "time_period": "PT72H"
            },
            {
                "name": "Тусить с друзьями",
                "id_user": User.objects.get(pk=1),
                "action": "Втретиться с друзьями",
                "time_begin": "2023-09-09T08:10:00",
                "place": "в баре",
                "is_pleasant_habit": "True",
                "time_limit": "PT168M",
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

