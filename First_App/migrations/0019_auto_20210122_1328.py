# Generated by Django 3.1.5 on 2021-01-22 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First_App', '0018_auto_20210112_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
