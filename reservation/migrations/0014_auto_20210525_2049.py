# Generated by Django 3.1.7 on 2021-05-25 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0013_reservation_rezdate1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='rezdate1',
            new_name='rezdate',
        ),
    ]
