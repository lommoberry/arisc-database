# arisc-database

Authors:
* Bridget Kim

Description
* Database for Balkan Academic research

Instructions
pip install django mysqlclient
* cd arisc-database
* cd arisc-database
* pip install -r requirements.txt
pip install pillow
* python -m django --version
* django-admin startproject mysite (makes webpage)
* python3 manage.py runserver (runs in development server)
* python3 manage.py startapp polls (makes an app)
* python3 manage.py migrate
* add to installed_apps in arisc-database/settings.py
* python manage.py makemigrations add
* By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

* Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk. 
* python manage.py sqlmigrate add 0001 (lets me see the sql of the models in add app)
* run migrate again
Playing with API
* python manage.py shell
* if port already in use error, netstat -ntlp, kill -9 PID
* or you can go to ports tab and kill