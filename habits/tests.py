from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from users.models import User


class HabitTestCases(APITestCase):
    """Тест кейс на создание новой привычки"""
    def setUp(self) -> None:

        self.client = APIClient()
        self.user = User.objects.create(
            email='ivan@ivanov.com',
            username='Ivan',
            password='Ivanov123',
        )
        self.client.force_authenticate(user=self.user)
        self.user.set_password('Ivanov123')
        self.user.save()

        self.habit_1 = Habit.objects.create(
            name="Test1",
            id_user=self.user,
            action="Test1",
            time_begin="2023-09-09T08:10:00",
            place="Test1",
            is_pleasant_habit="True",
            time_limit_seconds=120,
            time_period_days=2
        )
        self.habit_2 = Habit.objects.create(
            name="Test2",
            id_user=self.user,
            action="Test2",
            time_begin="2023-09-09T08:10:00",
            place="Test2",
            is_pleasant_habit="True",
            time_limit_seconds=120,
            is_public=True,
            time_period_days=2
        )

        self.habit_3 = Habit.objects.create(
            name="Test3",
            id_user=self.user,
            action="Test3",
            time_begin="2023-09-09T08:10:00",
            place="Test3",
            is_pleasant_habit="True",
            time_limit_seconds=120,
            time_period_days=2
        )

    def test_create_habit(self):
        """Тест создание привычки"""
        data = {
            "name": "Test",
            "id_user": self.user.id,
            "action": "Test",
            "time_begin": "2023-09-09T08:10:00",
            "place": "Test",
            "is_pleasant_habit": "True",
            "time_limit_seconds": 120,
            "is_public": True,
            "time_period_days": 2
        }

        responce = self.client.post(
            reverse('habits:habit_create'),
            data=data
        )
        # print(responce.json())
        self.assertEqual(
            responce.status_code,
            status.HTTP_201_CREATED
        )
        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_read_habit_list(self):
        """Тест на чтение списка привычек"""
        responce = self.client.get(
            reverse('habits:habit_list'),
        )

        self.assertEqual(
            responce.status_code,
            status.HTTP_200_OK
        )

    def test_read_single_habits(self):
        """Тест на чтение одной привычки"""
        responce = self.client.get(
            reverse('habits:habit_get', args=[self.habit_2.id]),
        )

        self.assertEqual(
            responce.status_code,
            status.HTTP_200_OK
        )

    def test_update_single_habits(self):
        """Тест Обновление одной привычки"""

        self.client = APIClient()
        self.user = User.objects.create(
            email='test@ivanov.com',
            username='test',
            password='test123',
        )
        self.client.force_authenticate(user=self.user)
        self.user.set_password('test123')
        self.user.save()

        self.habit_update = Habit.objects.create(
            name="Test1",
            id_user=self.user,
            action="Test1",
            time_begin="2023-09-09T08:10:00",
            place="Test1",
            is_pleasant_habit="True",
            time_limit_seconds=120,
            time_period_days=2
        )
        data = {
            "name": "Test update",
            "action": "Test update",
            "time_begin": "2023-11-13T08:10:00",
            "place": "Test update",
            "time_limit_seconds": 34,
            "time_period_days": 4
        }
        response = self.client.patch(
            reverse('habits:habit_update', args=[self.habit_update.id]),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_number_delete(self):
        """Тест удаление одной привычки"""

        response = self.client.delete(
            reverse('habits:habit_delete', args=[self.habit_1.id])
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class HabitValidatorCreateTestCase(APITestCase):
    """Тесты проверки Валидаторов"""
    def setUp(self) -> None:

        self.client = APIClient()
        self.user = User.objects.create(
            email='ivan@ivanov.com',
            username='Ivan',
            password='Ivanov123',
        )
        self.client.force_authenticate(user=self.user)
        self.user.set_password('Ivanov123')
        self.user.save()

        self.habit_2 = Habit.objects.create(
            name="Test2",
            id_user=self.user,
            action="Test2",
            time_begin="2023-09-09T08:10:00",
            place="Test2",
            is_pleasant_habit="True",
            time_limit_seconds=120,
            is_public=True,
            time_period_days=2
        )
        self.habit_no_pleasant = Habit.objects.create(
            name="Test2",
            id_user=self.user,
            action="Test2",
            time_begin="2023-09-09T08:10:00",
            place="Test2",
            time_limit_seconds=120,
            is_public=True,
            time_period_days=2
        )

    def test_Related_or_Award_HabitValidator(self):
        """Тест на ограничение: Исключить одновременный выбор связанной привычки и указания вознаграждения"""
        data = {
            "name": "Test",
            "id_user": self.user.id,
            "action": "Test",
            "time_begin": "2023-09-09T08:00:00",
            "place": "Test",
            "time_limit_seconds": 100,
            "time_period_days": 4,
            "award": "test",
            "related_habit": self.habit_2.id
        }

        responce = self.client.post(
            reverse('habits:habit_create'),
            data=data
        )

        self.assertEqual(
            responce.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_Time_Limit_HabitValidator(self):
        """Тест на ограничение: время выполнения должно быть не больше 120 секунд."""
        data = {
            "name": "Test",
            "id_user": self.user.id,
            "action": "Test",
            "time_begin": "2023-09-09T08:00:00",
            "place": "Test",
            "is_pleasant_habit": "True",
            "time_limit_seconds": 403,
            "time_period_days": 403
        }
        responce = self.client.post(
            reverse('habits:habit_create'),
            data=data
        )

        self.assertEqual(
            responce.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_Related_is_pleasant_habit_HabitValidator(self):
        """Тест на ограничение: В связанные привычки могут попадать только привычки с признаком приятной привычки"""
        data = {
            "name": "Test",
            "id_user": self.user.id,
            "action": "Test",
            "time_begin": "2023-09-09T08:00:00",
            "place": "Test",
            "time_limit_seconds": 100,
            "time_period_days": 4,
            "award": "test",
            "related_habit": self.habit_no_pleasant.id
        }
        responce = self.client.post(
            reverse('habits:habit_create'),
            data=data
        )

        self.assertEqual(
            responce.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_Pleasant_HabitValidator(self):
        """Тест на ограничение: У приятной привычки не может быть вознаграждения или связанной привычки"""
        data = {
            "name": "Test",
            "id_user": self.user.id,
            "action": "Test",
            "time_begin": "2023-09-09T08:00:00",
            "place": "Test",
            "time_limit_seconds": 100,
            "time_period_days": 4,
            "award": "test",
            "is_pleasant_habit": "True"
        }
        responce = self.client.post(
            reverse('habits:habit_create'),
            data=data
        )

        self.assertEqual(
            responce.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_Time_period_days_HabitValidator(self):
        """Тест на ограничение: Нельзя выполнять привычку реже, чем 1 раз в 7 дней"""
        data = {
            "name": "Test",
            "id_user": self.user.id,
            "action": "Test",
            "time_begin": "2023-09-09T08:00:00",
            "place": "Test",
            "time_limit_seconds": 100,
            "time_period_days": 400,
            "award": "test"
        }
        responce = self.client.post(
            reverse('habits:habit_create'),
            data=data
        )

        self.assertEqual(
            responce.status_code,
            status.HTTP_400_BAD_REQUEST
        )
