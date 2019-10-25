from django.db import models

# Create your models here.


class Student(models.Model):
    objects = None
    s_name = models.CharField(max_length=16)
    s_age = models.IntegerField(default=1)
