# Bank Guard Panel v2
Этот проект — вторая часть пульта охраны. Теперь все входы фиксируются системой пропусков, а сотрудники охраны следят за перемещениями в онлайн. 

## Что можно делать
- Видеть список всех сотрудников с пропусками.
- Переходить на каждого сотрудника и смотреть историю визитов.
- Видеть, кто сейчас находится внутри.
- Видеть, кто задерживается дольше обычного (по умолчанию — больше часа).

---

## Как запустить
1. Клонируйте репозиторий:
```
git clone https://github.com/maxchuk89/2_bank_guard_panel_part2.git
```

2. Создайте виртуальное окружение и активируйте его:
```
python -m venv venv
venv\Scripts\activate
```

3. Установите зависимости:
```
pip install -r requirements.txt
```

4. Создайте .env файл и добавьте в него настройки:
```
DEBUG=True
SECRET_KEY=ключ_для_криптоподписей_Django
ALLOWED_HOSTS=хосты_для_доступа_к_сайту
DB_ENGINE=движок_БД
DB_NAME=имя_БД
DB_USER=имя_пользователя_БД
DB_PASSWORD=пароль_пользователя_БД
DB_HOST=адрес_сервера_БД
DB_PORT=порт_подключения_к_БД
```

5. Запустите сервер:
```
python manage.py runserver 127.0.0.1:8000
```

6. Откройте сайт в браузере:
```
http://127.0.0.1:8000/
```
---