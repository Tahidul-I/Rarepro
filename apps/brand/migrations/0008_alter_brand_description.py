# Generated by Django 5.0 on 2024-02-03 11:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0007_alter_brand_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Add an ellaborate description abou the vendor'),
        ),
    ]
