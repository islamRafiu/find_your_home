# Generated by Django 4.1 on 2022-08-15 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20210411_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 15, 17, 10, 35, 841120)),
        ),
    ]
