# Generated by Django 3.2.9 on 2021-11-27 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_bookedtrips_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedTrips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default='0', max_length=200)),
                ('user_phone', models.CharField(default='', max_length=200)),
                ('user_email', models.CharField(default='', max_length=200)),
                ('trip_name', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
