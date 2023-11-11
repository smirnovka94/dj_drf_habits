from django.db import models

from django.conf import settings
from django.db import models


from users.models import NULLABLE, User


class Habit(models.Model):

    PERIOD_CHOICES = [
        ('MIN', 'Ежеминутная'),
        ('HOUR', 'Часовая'),
        ('DAY', 'Ежедневная'),
        ('WEEK', 'Еженедельная')
    ]

    name = models.CharField(max_length=100, verbose_name='название привычки')
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='создатель ',
                                **NULLABLE)
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='связанная привычка', **NULLABLE)
    action = models.CharField(max_length=100, verbose_name='действие')
    time_begin = models.DateTimeField(verbose_name='время начала привычки',**NULLABLE)
    place = models.CharField(max_length=30, verbose_name='место')
    is_pleasant_habit = models.BooleanField(default=False,verbose_name='признак_приятной_привычки',**NULLABLE)
    time_period = models.CharField(max_length=30, choices=PERIOD_CHOICES, default='DAY', verbose_name='периодичность привычки',**NULLABLE)
    award = models.CharField(max_length=30, verbose_name='вознаграждение',**NULLABLE)
    time_limit = models.DurationField(verbose_name='время на выполнение',**NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='признак_публичности',**NULLABLE)

    def __str__(self):
        return f'{self.name}: я буду ({self.action} в {self.time_begin} в [МЕСТО] {self.place})'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'