# Generated by Django 3.0.5 on 2020-12-25 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('icon', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='school',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=75)),
                ('universityEmail', models.EmailField(max_length=254)),
                ('personalEmail', models.EmailField(max_length=254)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.department')),
            ],
        ),
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=75)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.department')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.school'),
        ),
    ]
