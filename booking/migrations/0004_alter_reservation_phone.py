# Generated by Django 3.2.22 on 2023-10-17 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_reservation_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]