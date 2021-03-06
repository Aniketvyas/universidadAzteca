# Generated by Django 3.0.5 on 2021-01-19 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_auto_20210119_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateField()),
                ('caption', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='homeSlider',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='visionAndMission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
                ('category', models.CharField(choices=[('VISIONANDMISSION', 'VISION AND MISSION'), ('CHANCELORMESSAGE', 'CHANCELOR MESSAGE')], max_length=20)),
            ],
        ),
    ]
