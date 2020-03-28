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

api - > http://127.0.0.1:8000/user_activity/
result ->

{"response": [{"id": 1, "user__name": "Ashley Chang", "start_time": "2020-03-28T11:42:05Z", "end_time": "2020-03-28T11:42:05Z"}, {"id": 2, "user__name": "Kelly Manning", "start_time": "2020-03-28T11:42:05Z", "end_time": "2020-03-28T11:42:05Z"}, {"id": 3, "user__name": "Monica Ferguson", "start_time": "2020-03-28T11:42:05Z", "end_time": "2020-03-28T11:42:05Z"}, {"id": 4, "user__name": "Kelly Francis", "start_time": "2020-03-28T11:42:05Z", "end_time": "2020-03-28T11:42:05Z"}, {"id": 5, "user__name": "Danielle Fisher", "start_time": "2020-03-28T11:42:06Z", "end_time": "2020-03-28T11:42:06Z"}, {"id": 6, "user__name": "Tiffany Gregory", "start_time": "2020-03-28T11:42:06Z", "end_time": "2020-03-28T11:42:06Z"}, {"id": 7, "user__name": "Steve Powell", "start_time": "2020-03-28T11:42:06Z", "end_time": "2020-03-28T11:42:06Z"}, {"id": 8, "user__name": "Tammy King", "start_time": "2020-03-28T11:42:06Z", "end_time": "2020-03-28T11:42:06Z"}, {"id": 9, "user__name": "Carolyn Taylor", "start_time": "2020-03-28T11:42:06Z", "end_time": "2020-03-28T11:42:06Z"}, {"id": 10, "user__name": "Tamara Rogers", "start_time": "2020-03-28T11:42:06Z", "end_time": "2020-03-28T11:42:06Z"}]}
