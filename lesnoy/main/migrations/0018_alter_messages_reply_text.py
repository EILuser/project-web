# Generated by Django 5.0.6 on 2024-06-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_messages_reply_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='reply_text',
            field=models.TextField(default='Нет ответа', max_length=1000),
        ),
    ]
