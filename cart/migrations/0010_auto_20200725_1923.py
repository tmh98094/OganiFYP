# Generated by Django 3.0.8 on 2020-07-25 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_auto_20200725_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pickup_location',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='secondary_categories',
            field=models.ManyToManyField(blank=True, to='cart.Category'),
        ),
    ]
