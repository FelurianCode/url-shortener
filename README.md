# url-shortener
Simple url shortener in Django

## Requirements:
* Python3
* Django2.2.5
* djangorestframework
* mysql
* mysqlclient

### Installing requirements
```
python -m venv env && source env/bin/activate
pip install django
pip install djangorestframework
pip install mysqlclient
```

### Create empty database
```
CREATE DATABASE urls_db;

```

### Change your database config in:
url_shortener/settings.py


### Run migrations 
```
python manage.py migrate
```

### Run the project and get {YOUR_URL} 
```
python manage.py runserver
```


### Access here and shortener your URLs! :
```
http:/{YOUR_URL} 
```
