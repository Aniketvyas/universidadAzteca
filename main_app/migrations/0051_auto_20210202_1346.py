# Generated by Django 3.0.5 on 2021-02-02 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0050_maincampus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maincampus',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
