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
            # Рассчитываем количество дней с момента последней отправки
            days_since_last_sent = (now.date() - habit.last_sent_date).days if habit.last_sent_date else 0
            if days_since_last_sent >= 1:
                current_week_habit_count = habit.owner.habit_set.filter(period__gt=0).count()
                if current_week_habit_count < habit.period:
                    message = f"Нужно выполнить {habit.action} в {habit.place} в {habit.time}"
                    send_telegram_msg(habit.owner.tg_username, message)
                    # Обновляем последнюю дату отправки на сегодняшнюю
                    habit.last_sent_date = now.date()
                    habit.save()