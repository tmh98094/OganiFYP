# Generated by Django 3.0.8 on 2020-08-05 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0014_product_collected'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='collected',
        ),
    ]
