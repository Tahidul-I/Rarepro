# Generated by Django 5.0 on 2024-01-04 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image1', models.ImageField(upload_to='uploads/adds_image')),
                ('Image2', models.ImageField(upload_to='uploads/adds_image')),
            ],
        ),
    ]
