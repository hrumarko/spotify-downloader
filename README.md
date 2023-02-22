# Spotify Download
## Сервис по скачиванию музыки
### Суть сервиса
Пользователь вводит название трека, сервер идет на ютуб и скачивает в формате mp3 песню.Песня скачивается юзеру на ПК. Также есть вкладка с чартами где хранятся 50 треков популярных в стране в зависимости от IP пользователя. В качестве тестовового IP взят украинский адрес. Треки с чарта также можно скачать.

----

### Установка 
#### Натройка БД

```sudo -u postgres psql```

```CREATE DATABASE download_spotify;```

```CREATE USER marinov WITH ENCRYPTED PASSWORD '125785';```

```GRANT ALL PRIVILEGES ON DATABASE donwload_spotify TO marinov;```

----

#### Настройка проекта

+ Перейдите в желаемую директорию

```git clone https://github.com/hrumarko/spotify-downloader```

```cd spotify-downloader```

```python3 -m venv venv```

```source venv/bin/activate```

```cd config```

```pip install -r requirements.txt```

```python3 manage.py makemigrations```

```python3 manage.py migrate```

```python3 manage.py loaddata app.json```

```python3 manage.py runserver```

Go to ```http://127.0.0.1:8000/```

----

### Документация по тз

+ **SQL** 

  views.py
  строки `№ 21, 39, 59, 96, 108`
  
  models.py
  
+ **IP**

  views.py
  строка `№ 78`
  
+ **ООП**

  + MVC(MVT) - паттерн который используется в джанго
   
  + DRY, 
      
  создание методов `download_mp3()`, `get_url_video()`, `get_client_ip()` и пр. позволяют не повторятся, а просто вызвать данные методы, что делает код читабельнее
  + KISS
      
  использование готовых решений для капчи и взаимодействия с ютубом
 + **Работа с формами (создание, валидация)**
 
    forms.py
 + **Работа с файловой системой**
 
    папка media
    views.py 
    строки `№ 28, 60, 100`
  
 + **Регулярные выражения**
 
    строки `№ 73 74`
