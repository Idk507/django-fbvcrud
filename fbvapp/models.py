from django.db import models

# Create your models here.
class student(models.Model):
   # id = models.IntegerField()
    Subject = models.CharField(max_length=255)
    Date = models.DateField()