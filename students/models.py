from django.db import models

class Student(models.Model):
    first = models.CharField(max_length=20, default='')
    last = models.CharField(max_length=20, default='')
    email = models.CharField(max_length=20, default='')
