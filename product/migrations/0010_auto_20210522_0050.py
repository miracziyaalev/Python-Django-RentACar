# Generated by Django 3.1.7 on 2021-05-21 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20210522_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('New', 'Yeni'), ('True', 'Evet'), ('False', 'Hayır')], default='New', max_length=10),
        ),
    ]
