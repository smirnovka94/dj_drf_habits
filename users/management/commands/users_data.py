from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Класс пользователей.
    """
    def handle(self, *args, **kwargs):
        user = User.objects.create(
            username='1_user',
            email='1_user@mail.ru',
            password="qwerty88",
        )

        user.set_password("qwerty88")
        user.save()

