# Generated by Django 3.2.9 on 2021-12-04 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_savedtrips'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedtrips',
            name='trip_path',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='savedtrips',
            name='trip_path',
            field=models.CharField(default='', max_length=200),
        ),
    ]
