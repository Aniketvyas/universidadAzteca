# Generated by Django 3.0.5 on 2021-01-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0034_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]
