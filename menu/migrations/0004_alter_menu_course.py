# Generated by Django 3.2.22 on 2023-11-05 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20231030_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='course',
            field=models.CharField(choices=[('Antipasti', 'Antipasti'), ('Primi Piatti', 'Primi Piatti'), ('Secondi Piatti', 'Secondi Piatti'), ('Dolci', 'Dolci'), ('Bevande', 'Bevande')], max_length=50),
        ),
    ]