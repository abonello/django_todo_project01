# TODO app using Django

Using:  
* git  
* virtual environment with Python 3.6  
* Django   2.1

```bash
virtualenv venv -p python3
source venv/bin/activate
git init
pip freeze > Requirements.txt
```

versions:
```
pip 18.1
python 3.6.2
Django     2.1.3
pytz       2018.7
setuptools 40.5.0
wheel      0.32.2
```
---

Create folder to hold our app
```
mkdir my_app
```

Create the app
```
django-admin.py startproject todo_app .
```

Runserver to test the app is set up correctly
```
python manage.py runserver
```

Installation worked, everything is great and we are good to go.

Setting up the admin area by migrating the database that comes as standard.

```
python manage.py migrate
```

Now we can see the login screen for the django admin. We need a superuser.
```
python manage.py createsuperuser
```
### user: admin  
### password: 123pass456

Log into the admin area using the above credentials.

## Start building the app
```
python manage.py startapp todo_list
```

Register the todo_list app within our project todo_app. Open settings.py and add the todo_list app to the INSTALLED_APPS list 

---

## Start setting up the routing

Create a urls.py in our todo_list app.  
remove references to the admin in this newly created file.  

In the project's urls.py add include, and from the todo_list app import views. Then include the app's urls.py inside the project's urls.py
```python
from django.urls import path, include
from todo_list import views

urlpatterns = [
    . . .
    path('', include('todo_list.urls')),
]
```

---
## views.py file

The `urls.py` tells us **WHERE** our pages are.  
The `views.py` allows us to define **WHAT** our pages are.  

Import the views into this app's urls.py

```
from . import views
```
---

## Create the first view

Create a python function. We will call this view *home*. We need to pass in a request. This is anytime a web browser calls a web page. We will point this view to render the `home.html` template. The template is where the actual code for this page is going to be. We also need to pass in a dictionary which allows us to pass in data to our page.

```python
def home(request):
    return render(request, 'home.html', {})
```

___

## Create a template for our home route.

Creatte a `templates` folder inside the todo_list folder. Create a `home.html` file inside this new folder.

___

## Create the url

In this app's urls.py create a path that points to our view.

```python
path('', views.home, name='home'),
```

The name allows us to dynamically create links. We can reference these url patterns by name. The pattern is the first parameter.

___

## Creating a new page (About)

1. views.py - define route

```python
def about(request):
    return render(request, 'about.html', {})
```

2. urls.py - add url
```python
path('about/', views.about, name='about'),
```

3. Create new template - in templates folder create `about.html`.  
Place some stub code.
```html
<h1>This is the About Me page.</h1>
```

**NB: We will not be using this route in this project. Keep it for reference. I might extend the project later.**

---

## Templates and extending a Base template

Create a `base.html` file in the templates folder.
It uses jinja which allows us to use python-like code.

Connect base.html to home and about templates.

---

## Using Bootstrap framework

Copy starter template from bootstrap page and paste it in `base.html`.

NB: using bootstrap 4.1.3

```html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  </body>
</html>
```

Insert the block section in the body and wrap it in a div with class="container"

```html
<div class="container">
    {% block content %}
    {% endblock %}
</div>
```

---
## Dynamically change title of pages

Add a block title in the header of the page within the title tags.

NB. We can pass a different title for each page that will replace a default text defined in the base.

---
