# Generated by Django 3.1.7 on 2021-03-21 10:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evoting_app', '0007_auto_20210321_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 21, 16, 22, 39, 114439)),
        ),
    ]