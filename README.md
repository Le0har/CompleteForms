# Forms API

API форм шаблонов поиска по пришедшим полям

## Возможности Forms API

- Валидация пришедших полей
- Нахождение имени шаблона по пршедшим полям

## Технологии

- python 3.10+ - высокоуровневый язык программирования общего назначения
- django 5.1.3 - фреймворк для веб-приложений на языке Python
- djangorestframework 3.15.2 - фреймворк для разработки веб-API в приложениях на основе Django
- psycopg2-binary 2.9.10 - библиотека взаимодействия с СУБД PostgreSQL

## Установка на локальной машине

1. Клонировать репозиторий c GitHub
```
$ git clone https://github.com/Le0har/CompleteForms
```
2. Создать виртуальное окружение
```
$ python3 -m venv django_venv
```
3. Запустить виртуальное окружение
```
$ source django_venv/bin/activate
```
4. Обновить менеджер пакетов pip
```
$ python -m pip install --upgrade pip
```
5. Установить зависимости из ```requirements.txt```
```
$ pip install -r requirements.txt
```
6. Настроить подключение к БД (PostgreSQL) в файле ```settings.py```

- `ENGINE` - механизм, который используется для поключения к БД. В данном проекте - `django.db.backends.postgresql_psycopg2`
- `NAME` - имя БД
- `USER` - имя пользователя для подключения к БД
- `PASSWORD` - пароль для подключения к БД
- `HOST` - хост, на котором располагается БД. В данном проекте - `localhost`
- `PORT` - порт подключения к БД. В данном проекте - `5432`

7. Выполнить миграции
```
$ python manage.py migrate
```

8. Записать данные в БД (опционально)
```
$ python manage.py createdata
```

9. Запустить проект
```
$ python manage.py runserver
```

## Примеры запросов

- POST: /forms/get_form/

Request body:

```J-SON
{
  "email": "ivan@mail.hop",
  "phone": "+7 999 333 33 33"
}
```

Response:

```J-SON
{
  "form_name": "ShortForm"
}
```

- POST: /forms/get_form/

Request body:

```J-SON
{
  "email": "brus_li@mail.hop",
  "phone": "+7 999 444 44 44",
  "data": "2011-11-11",
  "text": "Цель не обязательно должна достигаться. Порой это лишь направление двигаться дальше."
}
```

Response:

```J-SON
{
  "form_name": "LongForm"
}
```

- POST: /forms/get_form/

Request body:

```J-SON
{
  "noemail": "brus_li@mail.hop",
  "phone": "+7 999 444 44 44",
  "datax": "2011-11-11",
  "textum": "Счастлив не тот, кто имеет всё лучшее, а тот, кто извлекает всё лучшее из того, что имеет."
}
```

Response:

```J-SON
{
  "form_name": "Unknown"
}
```

## Автор

Тихонов Алексей [https://github.com/Le0har](https://github.com/Le0har)