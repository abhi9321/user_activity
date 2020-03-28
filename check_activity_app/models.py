from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name


class ActivityPeriod(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


