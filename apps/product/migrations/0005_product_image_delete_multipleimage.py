# Generated by Django 5.0 on 2024-01-04 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_image_multipleimage_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='uploads/product_image'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='MultipleImage',
        ),
    ]
