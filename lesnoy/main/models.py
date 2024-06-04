from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Complaints(models.Model):
    class Meta:
        db_table = "complaints"
        verbose_name = "complaints"

    title = models.CharField(max_length=40, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    house_address = models.CharField(max_length=40, null=True)
    text = models.TextField(max_length=1000, null=True)
    
    def __str__(self):
        return self.title

class News(models.Model):
    class Meta:
        db_table = "news"
        verbose_name = "news"
    
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="main/static/image",null=True)
    publish_date = models.DateField(null=True)
    content = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.title