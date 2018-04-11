# djangorest

After cloning create a virtual env (inside the cloned dir) and then procced 
```
$ virtualenv <envname>
```


install required packages
```
$ pip3 install -r requirements.txt
```

remove the default db

```
$rm -f db.sqlite3
```

create a DB with defined models

```
$ python3 manage.py migrate
```

Create a superuser to access db using Admin

```
$ python3 manage.py createsuperuser
```

Runserver to access apis

```
$ python3 manage.py runserver
```


browse apis in 
http://localhost:8000/admin
http://localhost:8000/api
http://localhost:8000/api/<id>


