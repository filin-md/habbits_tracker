from datetime import timedelta

from django.utils import timezone

from config.celery import app
from main.models import Habit
from main.service_function import send_telegram_msg


@app.task()
def habit_notification():
    now = timezone.now()
    habits = Habit.objects.filter(time__gte=now, time__lte=now + timedelta(minutes=30))
    for habit in habits:
        message = f"Нужно выполнить {habit.action} в {habit.place} в {habit.time}"
        send_telegram_msg(habit.owner, message)