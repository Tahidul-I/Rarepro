# Generated by Django 5.0 on 2024-01-04 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_remove_subsubcategory_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subsubcategory',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
