# Generated by Django 3.0.5 on 2021-01-26 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0023_describingaccreditation_describingaccreditationparagraph'),
    ]

    operations = [
        migrations.CreateModel(
            name='accreditationImportance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
    ]
