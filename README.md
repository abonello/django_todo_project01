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

## Navbar

Adding a bootstrap navbar. Copy the code from bootstrap page and paste it in the `base.html`. We will change the style to `navbar-dark bg-dark`. Change the color of the button from *btn-outline-success* to `btn-outline-secondary`. 

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Dropdown
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="#">Action</a>
          <a class="dropdown-item" href="#">Another action</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">Something else here</a>
        </div>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#">Disabled</a>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
```

---
## Start changing the navbar

1. Change button text to **Add To List**.  
2. Change input placeholder to **To-Do Item**.  
3. Remove nav things we do not need.
    * Remove the Delete item
    * Remove the Dropdown item
4. Change the Link to **About**. For now use hard-coded href.
5. Remove the Home link.
6. Change Brand from Navbar to **To-Do List**. hard-code link to root.


### **Problem**: if we click on about link twice, we end up with a url of /about/about/ which will cause an error.

---

## Django dynamic links

Django links are better because they update dynamically.

We use jinja templating with `url` and the name of the view we used in `urls.py`.
```html
<a class="nav-link" href="{% url 'about' %}">About</a>
```

### **Bug Solved**: Now the error we had before disappears.

Do the same for the home link used with the brand name.
```html
<a class="navbar-brand" href="{% url 'home' %}">To-Do List</a>
```

Using dynamic links allows us to change the path of links without having to change the html code. Just change the path in the urls.py and leave the name as is.

---

## Context Dictionary

Example:

In the views.py
```python
def about(request):
    my_name = "Anthony Bonello"
    number = 2 + 2
    return render(request, 'about.html', {'name': my_name, 'number': number})
```
Then in the about.html page:
```html
{% block content %}
    <h1>This is the About Me page.</h1>
    <p>My name is {{ name }}.</p>
    <p>I am {{ number }} years old.</p>
{% endblock %}
```

If we want to pass on lots of key-value pairs we can create a dictionary which is conventionally called context which will hold all the data to be passed to the front end and just pass the context dictionary.

```python
def about(request):
    my_name = "Anthony Bonello"
    number = 2 + 2
    context = {'name': my_name, 'number': number}
    return render(request, 'about.html', context)
```

---

## Database - define a model

The main file to use is the `models.py`. We use a **python class**. The class should inherit from models.Model. Then define the data we need to store in the database. In our case we want to:
* have an item, 
* keep track if that item has been crossed-off the list (completed) or not.

When defining the data we define its data type. Each data type will take a number of parameters.

Also define a `__str__` method. This tells the class how it should represent itself. It is important for the admin page.

```python
from django.db import models

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item
```

---

## Database . . . continued

Creating a database is a three step process:
1. Create a model class
2. Create a migration
3. Push that migration into the database and make it live.

**Step 1** is done.  

**Step 2**: Next is create a migration. This will take the model (python class) and converts it into database language.

In a terminal, (inside the folder which holds manage.py, remember to have virtual environment active):

```bash
$ python manage.py makemigrations
Migrations for 'todo_list':
  todo_list/migrations/0001_initial.py
    - Create model List
```

Done!

If we look into the migrations folder we find a `0001_initial.py` file.
Contents:
```python
# Generated by Django 2.1.3 on 2018-11-06 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
```

Notice the name of the table and the addition of the id field.

**Step3**: in the terminal:
```bash
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, todo_list
Running migrations:
  Applying todo_list.0001_initial... OK
```

The database is ready to use.

---

## Add database to the admin section

Use the `admin.py` file and register our model. Start by importing our model `List` from `models.py`. 
```python
from .models import List
```

Next register it on the actual page. Pass in the name of the class to `admin.site.register`.

```python
admin.site.register(List)
```
---

## Conncet the database to the index page

1. Access the database from the `views.py` file. Import our **List** database model from `models.py`.

```python
from .models import List
```

Then pull out the data from the database and store it in a variable which can be passed into the context dictionary.

Data that are stored in a database are objects. We want all objects. Then pass it into the context dictionary.
```python
all_items = List.objects.all

return render(request, 'home.html', {'todo_items': all_items})
```

2. In the `home.html` template call the data in the context dictionary.

```html
{{ todo_items }}
```
This will give us:  
<QuerySet [<List: Finish this course | False>, <List: Feed the fish | False>, <List: See a video | True>]>

This can be improved by accessing each individual item by creating a loop.

There are various ways how we can display this data.
```html
{% block content %}
    <h3>All objects</h3>
    {{ todo_items }}
    <br>
    <hr>
    <br>
    <h3>Items as defined by __str__</h3>
    {% if todo_items %}
        <ul>
            {% for item in todo_items %}
                <li>{{ item }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>No items to display.</p>
    {% endif %}
    <br>
    <hr>
    <br>
    <h3>List of the item</h3>
    <p>Access the item directly</p>
    {% if todo_items %}
    <ul>
        {% for item in todo_items %}
        <li>{{ item.item }}</li>
        {% endfor %}
    </ul>
    {% else %}
    <p>No items to display.</p>
    {% endif %}

    <br>
    <hr>
    <br>
    <h3>Display in a table</h3>
    {% if todo_items %}
    <table class="table">
        <thead>
            <th>Item</th>
            <th>Completed</th>
        </thead>
        {% for item in todo_items %}
        <tr>
            <td>{{ item.item }}</td>
            <td>{{ item.completed }}</td>
        </tr>
        
        {% endfor %}
    </table>
    {% else %}
    <p>No items to display.</p>
    {% endif %}
{% endblock %}
```

___

## Decide on a layout and improve data display

We will use a table display. We will add a third column for Delete. This will be turned into a delete button later on. Add some bootstrap classes to improve layout and style.

If an item has been completed we want it to be styled differently. We will use `table-secondary` class which gives it a light grey background.

This is the code we have now:
```jinja
{% if todo_items %}
        <table class="table table-bordered">
            <thead class="thead-dark">
                <th>Item</th>
                <th><center>Completed</center></th>
                <th><center>Delete</center></th>
            </thead>
            {% for item in todo_items %}

            {% if item.completed %}
                <tr class="table-secondary">
            {% else %}
                <tr>
            {% endif %}
                <td>{{ item.item }}</td>
                <td><center>{{ item.completed }}</center></td>
                <td><center>Delete</center></td>
            </tr>
            
            {% endfor %}
        </table>
    {% else %}
        <p>No items to display.</p>
    {% endif %}
```

---

## Cross out completed items

We will use custom css to cross out completed items


1. In the top level directory of our project create a `static` directory. 

2. Inside the static directory create three new directories:
    1. css
    2. js
    3. images

3. Create a new file inside the css folder called `styles.css`.

4. We need to register the static directory in the `todo_app/settings.py`. Below the 
`STATIC_URL = '/static/'` entry add the following:
    ```python
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
    ```

Defining a path like this will make it computer agnostic. It does not matter what operating system you are using.

5. Create a style in our `style.css` file:
    ```css
    .striker {
        text-decoration: line-through;
    }
    ```

6. Link this css to our `base.html`.
    ```jinja
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
    ```

7. We need to give `base.html` the ability to load our static files. This is done by adding the following code at the very top of it.

```jinja
{% load static %}
```
---

## Enable the add item functionality

We need to turn the bootstrap add item form into a django form and register it with our app.

Create a `forms.py` file inside the todo_list app folder. It need to access our List model as well as django's forms.

forms.py
```python
from django import forms
from .models import List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]
```

Basically this is describing the model of our List class (the database).  
We can access ListForm by calling it within our views. For this to work we need to import this form into our `views.py`.

Now we can take information that is submitted through our form and manipulate it inside our view functions.

We need to prepare the navbar inside `base.html`. 
1. Find the form within the navbar code. Change the form's method to **POST**.
2. Add a cross-site request forgery token `{% csrf_token %}`
3. Add `name="item"`. This binds the input box with the item field of the model.

---

