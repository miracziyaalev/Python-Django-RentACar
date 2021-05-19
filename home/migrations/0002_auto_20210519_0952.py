# Generated by Django 3.1.7 on 2021-05-19 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='contact',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='aboutus',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='facebook',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='setting',
            name='instagram',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='setting',
            name='references',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='smtpemail',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='setting',
            name='smtppassword',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='setting',
            name='smtpport',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='setting',
            name='smtpserver',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='setting',
            name='twitter',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
