# Generated by Django 4.2.7 on 2023-11-30 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_max_price_car_price_remove_car_min_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_image',
            field=models.ImageField(blank=True, null=True, upload_to='car_images/'),
        ),
    ]
