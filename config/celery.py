from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установка переменной окружения для настроек проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создание экземпляра объекта Celery
app = Celery('config')

# Загрузка настроек из файла Django
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    "post_to_wb_rsa": {
        "task": "main.tasks.send_course_update_notification",
        "schedule": 60 * 10,
    },
}

