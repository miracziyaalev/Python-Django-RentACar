# Generated by Django 3.1.7 on 2021-06-18 11:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0047_auto_20210618_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='returndate',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='returntime',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='rezdate',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='reztime',
        ),
        migrations.AddField(
            model_name='reservation',
            name='reservationdate',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 18, 11, 50, 40, 203924, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='stopdate',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 18, 11, 50, 45, 719949, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
