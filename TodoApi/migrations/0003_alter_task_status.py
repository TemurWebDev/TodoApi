# Generated by Django 4.2.1 on 2023-05-08 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApi', '0002_task_delete_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('todo', 'Todo'), ('in_progress', 'In progress'), ('done', 'Done'), ('expired', 'Expired')], default='todo', max_length=20),
        ),
    ]