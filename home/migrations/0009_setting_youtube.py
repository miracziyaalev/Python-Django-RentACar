# Generated by Django 3.1.7 on 2021-05-26 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210526_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='youtube',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
