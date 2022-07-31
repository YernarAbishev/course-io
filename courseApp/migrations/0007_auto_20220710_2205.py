# Generated by Django 3.1 on 2022-07-10 16:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseApp', '0006_auto_20220710_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='postDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 10, 22, 5, 42, 420098)),
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('themeName', models.CharField(max_length=255, verbose_name='Theme name')),
                ('themeDescription', models.TextField(verbose_name='Theme description')),
                ('themeVideo', models.FileField(upload_to='', verbose_name='Video file')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseApp.course', verbose_name='Course')),
            ],
            options={
                'verbose_name_plural': 'Themes',
            },
        ),
    ]
