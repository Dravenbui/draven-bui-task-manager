# Generated by Django 3.1.6 on 2021-02-13 17:50

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('task_manager', '0003_auto_20210213_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='profile_photo',
            field=models.CharField(default='/static/media/project-logos/1.png', max_length=200),
        ),
    ]