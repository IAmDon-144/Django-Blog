# Generated by Django 3.1.3 on 2021-05-24 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=350, null=True),
        ),
    ]
