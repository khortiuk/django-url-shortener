# django-url-shortener
### app for shortener you url's
First we need to create virtual environment(optional)
```bash
virtualenv venv -p python3
```
And don't forget to activate it
```bash
source venv/bin/activate
```
Next step its install all requirements
```bash
pip install -r requirements.txt
```
Now we need to makemigrations and migrate it(by default use sqlite3)
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
If you want to get access to admin panel lets create superuser(optional)
```bash
python3 manage.py createsuperuser
```
Now we can run application
(on local machine by default its localhost:8000)
```bash
python3 manage.py runserver
```
(optional you can set which ip django app use)
```bash
python3 manage.py runserver 0.0.0.0:8000
```
Feel free to contribute and open issue