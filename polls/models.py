from django.db import models
from django import forms

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    login = models.CharField(max_length=25, verbose_name="Login")
    password = models.CharField(max_length=100, verbose_name="Password")
    phone = models.CharField(max_length=20, verbose_name="Phone number", null=True, default=None, blank=True)
    born_date = models.DateField(verbose_name="Born Date", null=True, default=None, blank=True)
    last_connection = models.DateTimeField(verbose_name="Date of last connection", null=True, default=None, blank=True)
    email = models.EmailField(verbose_name="email")
    years_seniority = models.IntegerField(verbose_name="Seniority", default=0)
    date_created = models.DateTimeField(verbose_name="Date of Birthday", auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(verbose_name="Project title", max_length=50)
    description = models.CharField(max_length=1000, verbose_name="Project description")
    client_name = models.CharField(max_length=1000, verbose_name="Client name")

    def __str__(self):
        return self.title


class Supervisor(UserProfile):
    specialization = models.CharField(max_length=50, verbose_name="Specialization")


class Developer(UserProfile):
    supervisor1 = models.ForeignKey(Supervisor, verbose_name="Supervisor", on_delete=models.CASCADE)


class Task(models.Model):
    title = models.CharField(verbose_name="Title", max_length=50)
    description = models.CharField(verbose_name="Description", max_length=1000)
    time_elapsed = models.IntegerField(verbose_name='Elapsed time', null=True, default=None, blank=True)
    importance = models.IntegerField(verbose_name="Importance")
    project = models.ForeignKey(Project, verbose_name="Project", null=True, default=None, blank=True, on_delete=models.CASCADE)
    developer = models.ForeignKey(Developer, verbose_name="User", on_delete=models.CASCADE)



