# Generated by Django 3.1.3 on 2021-05-23 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallary', '0014_auto_20210519_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='title',
            field=models.CharField(max_length=350),
        ),
    ]