# Generated by Django 5.0.1 on 2024-01-23 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0007_alter_todo_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='approaching_date',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
