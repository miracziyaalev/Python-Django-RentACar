# Generated by Django 3.1.7 on 2021-05-25 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0008_auto_20210525_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='rezdate',
            field=models.CharField(max_length=50),
        ),
    ]