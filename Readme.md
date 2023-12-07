# Установка и использование
Запустить Docker

Клонируем репозиторий

#### Устанавливаем виртуальное окружение 
```
python -m venv env
```
#### Запускаем Виртуальное окружение
```
env\Scripts\activate.bat
```

#### создаем бота в Telegramm BotFathe
получаем token to access the HTTP API

#### Создаем файл<.env>
.env.template переименовать на .env

#### Развернуть контейнер 
```
docker-compose build
```
#### Запустить контейнер 
```
docker-compose up
```
#### Если возникли проблемы создать базу данных в PgAdmin с именем <drf_habits>
```
docker-compose exec db psql -U postgres
create database drf_habits;
```
После чего повторить команду
```
docker-compose up
```