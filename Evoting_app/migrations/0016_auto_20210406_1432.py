# Generated by Django 3.1.7 on 2021-04-06 09:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evoting_app', '0015_auto_20210406_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 6, 14, 32, 31, 312840)),
        ),
        migrations.AlterField(
            model_name='voter',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 6, 14, 32, 31, 313826)),
        ),
    ]
