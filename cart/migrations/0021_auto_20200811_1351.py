# Generated by Django 3.0.8 on 2020-08-11 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0020_auto_20200811_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location_description',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='nutrition',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='pickup_location',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='primary_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_products', to='cart.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='produced',
            field=models.DateField(null=True),
        ),
    ]
