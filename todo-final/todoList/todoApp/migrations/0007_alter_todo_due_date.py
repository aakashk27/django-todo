# Generated by Django 5.0.1 on 2024-01-23 07:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0006_todo_due_date_alter_todo_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]