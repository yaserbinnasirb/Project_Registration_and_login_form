# Generated by Django 5.1.4 on 2024-12-08 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reglog',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('mobileno', models.IntegerField(max_length=11)),
            ],
        ),
    ]