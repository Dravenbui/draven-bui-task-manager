# Generated by Django 3.1.6 on 2021-02-13 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('members', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_manager.board')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('T', 'To Do'), ('D', 'Doing'), ('I', 'In Test'), ('O', 'Done'), ('B', 'Blocked'), ('L', 'Deleted')], max_length=1)),
                ('start_time', models.DateField(null=True)),
                ('end_time', models.DateField()),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_manager.project')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='members',
            field=models.ManyToManyField(through='task_manager.Project', to=settings.AUTH_USER_MODEL),
        ),
    ]
