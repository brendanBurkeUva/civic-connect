# Generated by Django 3.1.1 on 2020-11-08 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civic', '0004_emailtemp_sender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=200)),
            ],
        ),
    ]
