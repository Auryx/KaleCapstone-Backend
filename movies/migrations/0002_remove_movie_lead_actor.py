# Generated by Django 4.2.6 on 2023-10-13 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='lead_actor',
        ),
    ]
