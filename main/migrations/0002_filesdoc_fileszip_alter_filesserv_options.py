# Generated by Django 4.0.4 on 2022-05-11 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilesDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.FileField(max_length=255, upload_to='')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
        migrations.CreateModel(
            name='FilesZip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.FileField(max_length=255, upload_to='')),
                ('file_zip', models.FileField(max_length=255, upload_to='')),
            ],
            options={
                'verbose_name': 'Файл архива',
                'verbose_name_plural': 'Файлы архивов',
            },
        ),
        migrations.AlterModelOptions(
            name='filesserv',
            options={'verbose_name': 'Файл сертификата', 'verbose_name_plural': 'Файлы сертификатов'},
        ),
    ]
