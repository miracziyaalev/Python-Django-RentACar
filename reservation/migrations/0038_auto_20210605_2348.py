# Generated by Django 3.1.7 on 2021-06-05 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0037_auto_20210605_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='days',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='returnplace',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='rezplace',
        ),
    ]
