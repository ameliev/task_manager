from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    done = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} : {self.description} "


'''class UserTest(User):
    title = models.CharField(max_length=200)
    description = models.TextField()'''
