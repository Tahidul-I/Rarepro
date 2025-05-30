# Generated by Django 5.0 on 2024-02-01 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0009_delete_bannerbackground'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Click Checkbox To Activate'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='uploads/banner_image', verbose_name='Banner Image'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Give a suitable name'),
        ),
    ]
