# Generated by Django 3.1.3 on 2021-05-11 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallary', '0008_auto_20210511_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='subCat',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]