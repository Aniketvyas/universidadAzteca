# Generated by Django 3.0.5 on 2021-01-30 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0046_educationalmodalities_educationmodel_universityoffering'),
    ]

    operations = [
        migrations.CreateModel(
            name='educationalModalContent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='educationmodel',
            old_name='heading',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='educationmodel',
            name='content',
        ),
    ]
