# Generated by Django 3.1 on 2022-07-10 14:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='postDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 10, 20, 25, 24, 969445)),
        ),
    ]