# Generated by Django 3.1.7 on 2021-05-25 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0015_auto_20210525_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='rate',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]