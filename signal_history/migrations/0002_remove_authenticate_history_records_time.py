# Generated by Django 4.0.1 on 2022-01-10 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signal_history', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authenticate_history',
            name='records_time',
        ),
    ]
