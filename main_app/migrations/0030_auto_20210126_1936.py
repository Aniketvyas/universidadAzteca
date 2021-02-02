# Generated by Django 3.0.5 on 2021-01-26 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0029_accreditatedcenters_contactperson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accreditatedcenters',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='accreditatedcenters',
            name='contactPerson',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='accreditatedcenters',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='accreditatedcenters',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='accreditatedcenters',
            name='heading',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='accreditatedcenters',
            name='phoneNumber',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='accreditatedcenters',
            name='website',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
