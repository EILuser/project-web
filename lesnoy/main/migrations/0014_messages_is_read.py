# Generated by Django 5.0.6 on 2024-06-05 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_complaints_options_alter_news_options_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
