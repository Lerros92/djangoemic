# Generated by Django 3.0.9 on 2020-08-06 08:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baohanh', '0002_auto_20200806_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='deadline',
            field=models.DateField(default=datetime.date(2020, 8, 8)),
        ),
    ]
