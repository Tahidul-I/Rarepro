# Generated by Django 5.0 on 2024-01-06 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_remove_productvariation_original_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='size',
            field=models.CharField(max_length=100),
        ),
    ]
