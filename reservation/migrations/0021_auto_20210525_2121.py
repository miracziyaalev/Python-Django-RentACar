# Generated by Django 3.1.7 on 2021-05-25 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0020_auto_20210525_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='days',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='price',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='total',
        ),
    ]
