# Generated by Django 3.0.8 on 2020-07-17 07:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='product_images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='expired',
            field=models.DateField(),
        ),
    ]
