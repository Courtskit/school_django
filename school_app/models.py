from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=128)
    birthdate = models.DateField(default=None, null=True)