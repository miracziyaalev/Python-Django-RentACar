# Generated by Django 3.1.7 on 2021-05-27 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0027_auto_20210527_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='returnplace',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='rezplace',
        ),
    ]
