# Generated by Django 3.0.5 on 2021-01-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0035_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='designation',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
