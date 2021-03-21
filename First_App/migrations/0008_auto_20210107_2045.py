# Generated by Django 3.1.4 on 2021-01-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First_App', '0007_student_is_attend'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='studentImage')),
                ('is_attend', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_attend',
        ),
        migrations.AddField(
            model_name='student',
            name='attend',
            field=models.ManyToManyField(to='First_App.Attendent'),
        ),
    ]
