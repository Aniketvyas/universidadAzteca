# Generated by Django 3.0.5 on 2021-01-26 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0025_aftergraduationservices'),
    ]

    operations = [
        migrations.CreateModel(
            name='accreditatedCenters',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=100)),
                ('phoneNumber', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(max_length=50)),
            ],
        ),
    ]
