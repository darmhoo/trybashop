from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    orientation = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name

class Pages(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.TimeField()

