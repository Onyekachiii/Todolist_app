# Generated by Django 4.2.4 on 2023-09-04 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_task_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]