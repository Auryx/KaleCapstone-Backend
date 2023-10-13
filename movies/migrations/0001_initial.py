# Generated by Django 4.2.6 on 2023-10-13 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('lead_actor', models.CharField(max_length=100)),
                ('release', models.CharField(max_length=100)),
                ('pg_rating', models.CharField(max_length=100)),
                ('synopsis', models.CharField(max_length=100)),
            ],
        ),
    ]
