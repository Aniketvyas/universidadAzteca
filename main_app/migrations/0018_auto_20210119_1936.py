# Generated by Django 3.0.5 on 2021-01-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_visionandmission_heading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visionandmission',
            name='category',
            field=models.CharField(choices=[('VISIONANDMISSION', 'VISION'), ('CHANCELORMESSAGE', 'CHANCELOR MESSAGE'), ('MISSION', 'MISSION')], max_length=20),
        ),
    ]
