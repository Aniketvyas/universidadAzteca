# Generated by Django 3.0.5 on 2021-01-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_auto_20210119_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visionandmission',
            name='category',
            field=models.CharField(choices=[('VISION', 'VISION'), ('CHANCELORMESSAGE', 'CHANCELOR MESSAGE'), ('MISSION', 'MISSION')], max_length=20),
        ),
    ]
