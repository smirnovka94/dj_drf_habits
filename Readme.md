# Установка и использование
Клонируем репозиторий

Устанавливаем виртуальное окружение 
```
python -m venv env
```
Запускаем Виртуальнео окружение
```
env\Scripts\activate.bat
```
Устанавливаем библиотеки
```
pip install -r requirements.txt
```

Создаем базу данных в PgAdmin с именем <drf_test>
Создаем файл<.env>
.env.template переименовать на .env

#### Выполнить миграции
```
python manage.py makemigrations
python manage.py migrate
```
Загрузить базу данных
```
python manage.py loaddata users_data.json
python manage.py loaddata course_data.json
python manage.py loaddata lesson_data.json


```
Создаем superuser
login: kirill@sky.pro
password: qwerty88
```
python manage.py super_user
```
