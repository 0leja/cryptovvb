# Generated by Django 4.0.4 on 2022-05-12 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_filesdecrypt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filesdecrypt',
            name='doc',
            field=models.FileField(max_length=255, upload_to='decrypt/'),
        ),
    ]
