from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Complaints(models.Model):
    class Meta:
        db_table = "complaints"

    title = models.CharField(max_length=40, help_text="Введите тему жалобы", default="Жалоба")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    house_address = models.CharField(max_length=40, help_text="Введите адрес дома, в котором проживаете", default="Адрес")
    text = models.TextField(max_length=1000, help_text="Оставьте свою жалобу", default="Текст жалобы")

    def get_absolute_url(self):
        return reverse("complaints-detail", args=[str(self.id)])
    
    def __str__(self):
        return self.title