# Generated by Django 3.1.6 on 2021-02-13 16:39

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('task_manager', '0002_auto_20210213_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.CharField(max_length=500),
        ),
        migrations.DeleteModel(
            name='Members',
        ),
    ]
