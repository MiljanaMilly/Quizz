# Quizz Application

# Getting Started

Aplikacija je radjena u IDE PyCharm, korisceni su: 
- Python 3.10.6
- Django 3.1.3
- MySQL server (kroz XAMPP v3.2.4)
- Bootstrap 5 CDN


Potrebno je pokrenuti MySQL server i kreirati bazu sa sledecim parametrima:

    'NAME': 'quizz',
    'USER': 'root',
    'PASSWORD': 'root',
    'HOST': '127.0.0.1',
    'PORT': '3301'

Parametre je moguce izmeniti i u fajlu: quiz_project/project/settings.py


Potrebno je klonirati projekat sa GitHub-a:
URL: https://github.com/MiljanaMilly/Quizz.git

    $ git clone git@github.com/MiljanaMilly/Quizz.git


Kreiranje migracija baze:

    $ python manage.py makemigrations

Primeniti migracije baze:

    $ python manage.py migrate
    

Pokrenite aplikaciju :

    $ python manage.py runserver

Aplikacija je dostupna na :

     http://127.0.0.1:8000/