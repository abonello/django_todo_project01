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
