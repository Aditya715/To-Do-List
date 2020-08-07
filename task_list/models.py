from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=500)
    schedule = models.DateField()
    status = models.CharField(max_length=20, default='open')
