# Generated by Django 3.1.3 on 2021-05-11 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallary', '0009_auto_20210511_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='catagory',
            field=models.ManyToManyField(default=None, related_name='catagory', to='gallary.Catagory'),
        ),
    ]
