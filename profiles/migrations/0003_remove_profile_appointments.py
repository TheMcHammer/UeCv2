# Generated by Django 3.0.2 on 2020-07-13 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20200713_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='appointments',
        ),
    ]
