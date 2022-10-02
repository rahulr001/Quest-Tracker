# Generated by Django 4.1 on 2022-09-29 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0006_alter_task_taskdesc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('working on it', 'Working on it'), ('stuck', 'Stuck'), ('done', 'Done')], default='Working on it', max_length=30),
        ),
    ]
