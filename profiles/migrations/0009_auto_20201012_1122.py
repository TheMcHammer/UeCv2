# Generated by Django 3.0.2 on 2020-10-12 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20201012_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
        migrations.AlterField(
            model_name='profile',
            name='course',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
