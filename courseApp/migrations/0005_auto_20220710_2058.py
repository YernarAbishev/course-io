# Generated by Django 3.1 on 2022-07-10 14:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseApp', '0004_auto_20220710_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='courseCategory',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='course',
            name='postDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 10, 20, 58, 17, 927651)),
        ),
    ]
