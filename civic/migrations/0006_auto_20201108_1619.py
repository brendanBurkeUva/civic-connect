# Generated by Django 3.1.1 on 2020-11-08 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('civic', '0005_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='ad',
            new_name='address',
        ),
    ]
