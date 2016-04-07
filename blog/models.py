from __future__ import unicode_literals

from django.db import models


# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.IntegerField()
    intime = models.DateTimeField()

    class Meta:
        db_table = 'student'


class teacher(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'teacher'
