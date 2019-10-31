from django.db import models

# Create your models here.


class Person(models.Model):
    p_name = models.CharField(max_length=16)
    p_sex = models.BooleanField(default=False)


class IDcard(models.Model):
    id_num = models.CharField(max_length=18, unique=True)
    id_person = models.OneToOneField(Person, null=True, on_delete=models.CASCADE)


class Animal(models.Model):
    a_name = models.CharField(max_length=16)

    class Meta:
        abstract = True


class Cat(Animal):
    c_eat = models.CharField(max_length=32)


class Dog(Animal):
    d_legs = models.CharField(max_length=4)