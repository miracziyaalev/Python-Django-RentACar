# Generated by Django 3.1.7 on 2021-05-25 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0018_auto_20210525_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='days',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='price',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='total',
            field=models.IntegerField(blank=True),
        ),
    ]
