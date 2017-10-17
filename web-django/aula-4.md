---
author: Prof. Iury Adones
title: PYTHON DJANGO 
---

# INTRODUÇÃO AO DJANGO

## INSTALL DJANGO

```bash
$ python --version
Python 3.6.2
$ pip install Django==1.11.6
$ python -m django --version
1.11.6
```

## START PROJECT

```bash
$ django-admin startproject stox
```

## TREE

```bash
.
└── stox
    ├── manage.py
    └── stox
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

## CD PROJECT

```bash
$ cd stox
```

## RUNSERVER

```bash
$ python manage.py runserver
```

```bash
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). 
Your project may not work properly until you apply
the migrations for app(s): admin, auth, contenttypes,
sessions.
Run 'python manage.py migrate' to apply them.

October 14, 2017 - 19:27:29
Django version 1.11.6, using settings 'stox.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

---

![Page default](./images/starting_django.png){width=400% height=400%}

---

## SETTING PORT

```bash
$ python manage.py runserver 8080
```

```bash
$ python manage.py runserver 0:8080
```

```bash
$ python manage.py runserver 0.0.0.0:8080
```

## STARTAPP

```bash
$ python manage.py startapp core
```

## TREE

```bash
core
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```

---

core/views.py

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá, mundo!")
```

---

core/urls.py

```python
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```

---

`<project>/urls.py`

stox/urls.py

```python
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^core/', include('core.urls')),
    url(r'^admin/', admin.site.urls),
]
```

---

![ooohhh](./images/core.png){width=400% height=400%}


# POSTGRESQL/MYSQL

# DJANGO (MYSQL/POSTGRESQL)

# WEBSERVICES

