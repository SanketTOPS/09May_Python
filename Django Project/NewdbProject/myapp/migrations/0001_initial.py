# Generated by Django 5.0.7 on 2024-08-06 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('mobile', models.BigIntegerField()),
                ('address', models.TextField()),
            ],
        ),
    ]
