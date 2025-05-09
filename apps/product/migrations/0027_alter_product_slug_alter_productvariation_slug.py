# Generated by Django 5.0 on 2024-02-03 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_alter_product_options_alter_productimages_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, help_text='No need to fill out this field', max_length=500, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='slug',
            field=models.SlugField(blank=True, help_text='No need to fill out this field', max_length=500, null=True, unique=True),
        ),
    ]
