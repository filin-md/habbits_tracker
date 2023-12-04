from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    tg_username = models.CharField(max_length=255, verbose_name='ник телеграм')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Habit(models.Model):
    place = models.CharField(max_length=100, verbose_name='место выполнения привычки', null=True, blank=True)
    time = models.TimeField(verbose_name='время выполнения привычки', null=True, blank=True)
    action = models.CharField(max_length=100, verbose_name='действие привычки')
    is_pleasant = models.BooleanField(verbose_name='приятная или нет', null=True, blank=True)
    linked = models.ForeignKey('self', verbose_name='связанная привычка', on_delete=models.SET_NULL, null=True, blank=True)
    period = models.PositiveSmallIntegerField(verbose_name='сколько раз в неделю')
    reward = models.CharField(max_length=100, verbose_name='награда', null=True, blank=True)
    length = models.PositiveIntegerField(verbose_name='время выполнения в секундах')
    is_public = models.BooleanField(verbose_name='публичная или приватная')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец привычки')

