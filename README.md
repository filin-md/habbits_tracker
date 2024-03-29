# Трекер полезных привычек


Контекст:
В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. 
В рамках проекта реализована бэкенд-часть SPA API веб-приложения трекер полезных привычек.

Характеристики:

-CORS.

-Интеграция с Telegram.

-Пагинация - список привычек выводится по 5 привычек на страницу.

-Переменные окружения.

-Все необходимые модели описаны или переопределены.

-Реализованы необходимые эндпоинты:

--Регистрация

--Авторизация

--Список привычек текущего пользователя с пагинацией

--Список публичных привычек

--Создание привычки

--Редактирование привычки

--Удаление привычки

-Настроены все необходимые валидаторы:

--Исключены одновременный выбор связанной привычки и указание вознаграждения.

--Время выполнения должно быть не больше 120 секунд.

--В связанные привычки могут попадать только привычки с признаком приятной привычки.

--У приятной привычки не может быть вознаграждения или связанной привычки.

--Нельзя выполнять привычку реже, чем 1 раз в 7 дней.

-Описанные права доступа заложены:

--Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.

--Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.

-Настроена отложенная задача через Celery.

-Имеется список зависимостей.

-Результат проверки Flake8 равен 100%, при исключении миграций.


Инструкция по установке:


1 Скачать архив

2 распаковать

3 Установить Docker, если не был установлен - https://www.docker.com/get-started/

4 Открыть терминал в папке проекта

5 Выполнить команду docker-compose build

6 Выполнить команду docker-compose up

7 Перейти в браузере по адресу 127.0.0.1:8001/swagger
