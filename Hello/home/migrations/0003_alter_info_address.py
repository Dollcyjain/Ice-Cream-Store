# Generated by Django 4.1.7 on 2023-03-18 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='address',
            field=models.TextField(max_length=162),
        ),
    ]
