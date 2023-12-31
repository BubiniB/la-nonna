# Generated by Django 3.2.22 on 2023-10-16 12:04

import datetime
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('party', models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='2', max_length=50)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('time', models.CharField(choices=[('18:00', '18:00'), ('18:15', '18:15'), ('18:30', '18:30'), ('18:45', '18:45'), ('19:00', '19:00'), ('19:15', '19:15'), ('19:30', '19:30'), ('19:45', '19:45'), ('20:00', '20:00'), ('20:15', '20:15'), ('20:30', '20:30'), ('20:45', '20:45')], max_length=10)),
            ],
        ),
    ]
