# Generated by Django 2.2 on 2020-08-04 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_list', '0003_task_open'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='open',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default='open', max_length=20),
        ),
    ]