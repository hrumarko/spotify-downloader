# Generated by Django 4.1.5 on 2023-02-20 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download_spotify', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Files',
            new_name='File',
        ),
    ]
