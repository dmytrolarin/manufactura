# Generated by Django 4.0.4 on 2022-06-23 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_alter_tablereservation_date_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablereservation',
            name='date_reservation',
            field=models.IntegerField(verbose_name='Дата бронювання'),
        ),
    ]
