# Generated by Django 3.0.2 on 2020-09-30 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='course',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='year',
            field=models.IntegerField(default=1),
        ),
    ]
