#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
"""

    *** Lec_3 ***
$ django-admin startproject project-name
to start a project

manage.py   the manager of the projects
urls.py    table of contents for our web application


$ python3 manage.py runserver
runs the server

$ python3 manage.py startapp app-name
starts a new app within the project

setting.py    default configuration of a django project

to add an app go to settings.py and add its name

INSTALLED_APPS = [
    "hello",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

in hello/views.py you configure the looks of the project
eg:

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("hello world")


then in hello create urls.py to add different URLs
eg:

from django.urls import path
from . import views
# because they are located in the same directory


urlpatterns =[
    path("", views.index, name="index")
]


then you should edit the main urls.py in the
main folder of the project
eg:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('hello/',include("hello.urls"))
]



then when you run the original runserver command
$ python3 manage.py runserver

and go to http://127.0.0.1:8000/hello/
you should be able to see the "hello owrld" message


to add a new path to hello
in views.py:

def index(request):
    return HttpResponse("hello")

def parsa(request):
    return HttpResponse("hello,parsa")

go to hello/urls.py

urlpatterns =[
    path("", views.index, name="index"),
    path("parsa",views.parsa, name= "parsa")
]

and the runserver
and http://127.0.0.1:8000/hello/parsa

you can personalize it like
http://127.0.0.1:8000/hello/cat
http://127.0.0.1:8000/hello/ali
http://127.0.0.1:8000/hello/john
http://127.0.0.1:8000/hello/kianmher

in which all those are executed under a greet function


in views.py

def index(request):
    return HttpResponse("hello")
def parsa(request):
    return HttpResponse("hello,parsa")
def greet(request, name):
    return HttpResponse(f"hello {name}")

in hello/urls.py

urlpatterns =[
    path("", views.index, name="index"),
    path("parsa",views.parsa, name= "parsa"),
    path("<str:name>",views.greet, name="greet")
]


    *** html pages arrive! ***

so in views.py you should return this
def index(request):
    return render(request, "hello/index.html")

where the path starts from the lec_3/hello/templates directory :)
the design of templates folder is questionable :)

be sure to create the templates directory and add the said html


    *** adding variables to HTML (django template language) ***

in views.py

def index(request):
    return render(request, "hello/index.html",{
        "name" : parsa
    })

in index.html

you have logged in as {{ username }}


    *** python logic in html ***

as we saw we give variables to html with 

def index(request):
    return render(request,"newyear/index.html",{
        "phrase": "parsa",
        "n" : 12
    })

we can do python logic in html with:

{% if n > 50 %}
    the number {{n}} is bigger than 50
{% else %}
    the number {{n}} is smaller than 50
{% endif %}



    *** CSS arrives at the Scene! ***

firt remember to create an static directory
remmber the app-name directory
inside make your css file (here styles.css)

and in the html file:

{% load static %}   # remember to do this

<!doctype html>
<html lang="en">
    <link rel="stylesheet" href="newyear/styles.css">
    <head>
        newyear
    </head>
    <body>
        <h1>
        {% if n > 50 %}
            the number {{n}} is bigger than 50
        {% else %}
            the number {{n}} is smaller than 50
        {% endif %}
        </h1>
    </body>
</html>






















"""




import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lec_3.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
