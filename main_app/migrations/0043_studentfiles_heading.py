# Generated by Django 3.0.5 on 2021-01-30 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0042_studentfiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentfiles',
            name='heading',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]