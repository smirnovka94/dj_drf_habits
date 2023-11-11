from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = models.CharField(max_length=150,unique=True,verbose_name='username')
    email = models.EmailField(unique=True, verbose_name='email')
    password = models.CharField(max_length=100,verbose_name='password')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}({self.username}, password - {self.password})'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'