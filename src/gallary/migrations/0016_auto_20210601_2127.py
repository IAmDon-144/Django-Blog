# Generated by Django 3.1.3 on 2021-06-01 15:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallary', '0015_auto_20210523_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
