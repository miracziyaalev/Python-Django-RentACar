# Generated by Django 3.1.7 on 2021-05-31 15:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0032_auto_20210531_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='return_reservation_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 5, 31, 15, 16, 20, 621544, tzinfo=utc)),
            preserve_default=False,
        ),
    ]