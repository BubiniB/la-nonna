# Generated by Django 3.2.22 on 2023-10-17 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_rename_party_reservation_number_of_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='phone',
            field=models.IntegerField(),
        ),
    ]