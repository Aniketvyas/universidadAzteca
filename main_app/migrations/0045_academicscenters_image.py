# Generated by Django 3.0.5 on 2021-01-30 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0044_academicscenters'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicscenters',
            name='image',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
