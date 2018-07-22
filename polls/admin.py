from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.Supervisor)
admin.site.register(models.Task)
admin.site.register(models.Developer)
admin.site.register(models.Project)
