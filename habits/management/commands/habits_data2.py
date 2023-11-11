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
                "related_habit": Habit.objects.get(pk=1),
                "time_limit": "PT30M",
            },
        ]

        habit_for_create = []
        for habit_item in habits_list:
            habit_for_create.append(
                Habit(**habit_item)
            )


        Habit.objects.bulk_create(habit_for_create)
        print(habit_for_create)

