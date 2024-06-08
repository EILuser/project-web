from django.contrib import admin
from . import models

admin.site.register(models.Complaints)
admin.site.register(models.News)
admin.site.register(models.Messages)
admin.site.register(models.MeterReadings)