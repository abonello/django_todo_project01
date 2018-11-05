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