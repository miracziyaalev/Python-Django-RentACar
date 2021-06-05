# Generated by Django 3.1.7 on 2021-05-26 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_remove_category_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='banner',
            field=models.CharField(choices=[('Banner1', 'Banner1'), ('Banner2', 'Banner2'), ('Banner3', 'Banner3')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='modelyear',
            field=models.CharField(default=2020, max_length=30),
            preserve_default=False,
        ),
    ]