import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_activity.settings')

import django

django.setup()

# fake populate
from check_activity_app.models import User, ActivityPeriod
from faker import Faker

fakeObj = Faker()

def add_topic():
    t = User.objects.get_or_create(name=fakeObj.name())[0]
    t.save()
    return t

def populate(N):
    for entry in range(N):
        top = add_topic()
        fake_name = fakeObj.name()
        fake_start_time = fakeObj.date_time_between_dates(datetime_start=None, datetime_end=None, tzinfo=None)
        fake_end_time = fakeObj.date_time_between_dates(datetime_start=fake_start_time, datetime_end=None, tzinfo=None)
        rec = ActivityPeriod.objects.get_or_create(start_time=fake_start_time, end_time=fake_end_time, user=top)[0]


if __name__ == '__main__':
    print("populating db with fake data")
    populate(10)

