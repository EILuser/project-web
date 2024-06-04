# Generated by Django 5.0.6 on 2024-06-03 19:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaints',
            name='address',
        ),
        migrations.RemoveField(
            model_name='complaints',
            name='email',
        ),
        migrations.RemoveField(
            model_name='complaints',
            name='full_name',
        ),
        migrations.AddField(
            model_name='complaints',
            name='house_address',
            field=models.CharField(default='Адрес', help_text='Введите адрес дома, в котором проживаете', max_length=40),
        ),
        migrations.AddField(
            model_name='complaints',
            name='title',
            field=models.CharField(default='Жалоба', help_text='Введите тему жалобы', max_length=40),
        ),
        migrations.AddField(
            model_name='complaints',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='text',
            field=models.TextField(default='Текст жалобы', help_text='Оставьте свою жалобу', max_length=1000),
        ),
    ]