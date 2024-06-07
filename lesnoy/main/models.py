from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Complaints(models.Model):
    class Meta:
        db_table = "complaints"
        verbose_name = "complaint"
        verbose_name_plural = "complaints"

    title = models.CharField(max_length=40, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_date = models.DateField(null=True)
    house_address = models.CharField(max_length=40, null=True)
    text = models.TextField(max_length=1000, null=True)
    
    def __str__(self):
        return self.title

class News(models.Model):
    class Meta:
        db_table = "news"
        verbose_name = "news"
        verbose_name_plural = "news"
    
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="news/",null=True)
    publish_date = models.DateField(null=True)
    content = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.title

class Messages(models.Model):
    class Meta:
        db_table = "messages"
        verbose_name = "message"
        verbose_name_plural = "messages"
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    send_date = models.DateTimeField(null=True)
    title = models.CharField(max_length=40, null=True)
    question_text = models.TextField(max_length=1000, null=True)
    reply_text = models.TextField(max_length=1000, default="Нет ответа")
    reply_date = models.DateTimeField(null=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class MeterReadings(models.Model):
    class Meta:
        db_table = "meter_readings"
        verbose_name = "meter_reading"
        verbose_name_plural = "meter_readings"
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    send_date = models.DateField(null= True)
    # Номер лицевого счета
    personal_account = models.CharField(max_length=9, null=True)
    hot_watter_supply = models.IntegerField(null=True)
    cold_watter_supply = models.IntegerField(null=True)
    gas_supply = models.IntegerField(null=True)
    electricity_supply = models.IntegerField(null=True)
    
    def __str__(self):
        return self.personal_account