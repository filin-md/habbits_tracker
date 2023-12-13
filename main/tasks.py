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
            days_since_last_sent = (now.date() - habit.last_sent_date).days if habit.last_sent_date else (now.date() - habit.created_at).days
            message = f"Нужно выполнить {habit.action} в {habit.place} в {habit.time}"

            if days_since_last_sent >= 1:

                if days_since_last_sent >= 7:
                    send_telegram_msg(habit.owner.tg_username, message)
                    habit.last_sent_date = now.date()
                    habit.save()
                    return
                if days_since_last_sent >= 30:
                    send_telegram_msg(habit.owner.tg_username, message)
                    habit.last_sent_date = now.date()
                    habit.save()
                    return

                send_telegram_msg(habit.owner.tg_username, message)
                habit.last_sent_date = now.date()
                habit.save()
                return
