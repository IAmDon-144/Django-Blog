# Generated by Django 3.1.3 on 2021-05-11 17:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallary', '0010_auto_20210511_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='image1',
            field=models.ImageField(blank=True, upload_to='gallary', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AddField(
            model_name='images',
            name='image2',
            field=models.ImageField(blank=True, upload_to='gallary', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AddField(
            model_name='images',
            name='image3',
            field=models.ImageField(blank=True, upload_to='gallary', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
    ]