# create and activate virtual env
python3 -m venv venv
source venv/bin/activate

# project name : user_activity
django-admin startproject user_activity
cd user_activity/
(venv) agopalaiah-ltm:user_activity agopalaiah$ python manage.py  runserver

# create app = check_activity_app
(venv) agopalaiah-ltm:user_activity agopalaiah$ python manage.py startapp check_activity_app

# register check_activity_app in settings.py
# create models

python manage.py migrate
python manage.py makemigrations check_activity_app

python manage.py migrate

# populate data
pip install Faker

run populate_app.py to populate the db
python populate_app.py

# create api
# in url.py include below line
path('user_activity/', views.index, name='index'),

python manage.py runserver

