# Generated by Django 3.0.5 on 2021-01-17 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='degreeProgram',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('specializationAvailable', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='educationalOffering',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='eligibility',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('note', models.TextField()),
                ('degreeProgram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.degreeProgram')),
            ],
        ),
        migrations.CreateModel(
            name='policy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=400)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='policyDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('tags', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='refundCharges',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='refundSteps',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='specialization',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('degreeProgram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.degreeProgram')),
            ],
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='department',
        ),
        migrations.RemoveField(
            model_name='student',
            name='department',
        ),
        migrations.DeleteModel(
            name='department',
        ),
        migrations.DeleteModel(
            name='faculty',
        ),
        migrations.DeleteModel(
            name='school',
        ),
        migrations.DeleteModel(
            name='student',
        ),
        migrations.AddField(
            model_name='degreeprogram',
            name='educationalOffering',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.educationalOffering'),
        ),
    ]