# Generated by Django 3.0.5 on 2021-01-28 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0038_thesispolicy'),
    ]

    operations = [
        migrations.CreateModel(
            name='academyWorks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('icon', models.FileField(blank=True, upload_to='')),
                ('attachment', models.FileField(blank=True, upload_to='')),
            ],
        ),
    ]
