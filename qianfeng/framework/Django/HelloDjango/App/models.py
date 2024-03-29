from django.db import models


# Create your models here.


class Student(models.Model):
    objects = None
    s_name = models.CharField(max_length=16)
    s_age = models.IntegerField(default=1)


class Person(models.Model):
    p_name = models.CharField(max_length=16, unique=True)
    p_age = models.IntegerField(default=18, db_column='age')
    p_sex = models.BooleanField(default=False, db_column='sex')
    p_hobby = models.CharField(max_length=32, null=True, blank=True)

    @classmethod
    def create(cls, p_name='hjl', p_age=100, p_sex=True, p_hobby='gaming'):
        return cls(p_name=p_name, p_age=p_age, p_sex=p_sex, p_hobby=p_hobby)

    class Meta:
        db_table = 'People'
