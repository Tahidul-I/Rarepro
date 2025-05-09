# Generated by Django 5.0 on 2024-02-04 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0028_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=50, verbose_name='SKU'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='uploads/product_image', verbose_name='Product Thumbnail'),
        ),
    ]
