# Generated by Django 3.0.5 on 2021-01-26 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0026_accreditatedcenters'),
    ]

    operations = [
        migrations.AddField(
            model_name='accreditatedcenters',
            name='country',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]