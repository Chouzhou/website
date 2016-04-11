from __future__ import unicode_literals

from time import timezone

from django.db import models


# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'teacher'

    def __unicode__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.IntegerField()
    intime = models.DateField()
    teacher = models.ForeignKey(Teacher, related_name='student_teacher')

    class Meta:
        db_table = 'student'

    def __unicode__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(Student, through="MemberShip")

    class Meta:
        db_table = 'group'


class MemberShip(models.Model):
    student = models.ForeignKey(Student)
    group = models.ForeignKey(Group)

    class Meta:
        db_table = 'membership'
