# Generated by Django 3.1.3 on 2021-05-19 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallary', '0013_auto_20210519_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='subCat',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
