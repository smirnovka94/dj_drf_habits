# Установка и использование
Клонируем репозиторий

#### Устанавливаем виртуальное окружение 
```
python -m venv env
```
#### Запускаем Виртуальное окружение
```
env\Scripts\activate.bat
```
#### Устанавливаем библиотеки
```
pip install -r requirements.txt
```

#### Создаем базу данных в PgAdmin с именем <drf_test>
Создаем файл<.env>
.env.template переименовать на .env

#### Выполнить миграции
```
python manage.py makemigrations
python manage.py migrate
```

#### Создаем superuser
login: kirill@sky.pro
password: qwerty88
```
python manage.py super_user
```

#### Загрузить базу данных
```
python manage.py users_data
python manage.py habits_data1
python manage.py habits_data2
```
#### Добавить пользователям ID Телеграмм чата
заполнить параметр: User.telegram_id

#### Локальный тест файл для отправлки сообщения в телеграмм
```
python manage.py test_run_send_TG
```