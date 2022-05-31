# Generated by Django 4.0.4 on 2022-05-31 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_product_composition'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255, verbose_name="Ім'я клієтна")),
                ('client_phone_number', models.IntegerField(verbose_name='Номер телефону')),
                ('time_reservation', models.TimeField(verbose_name='Час бронювання')),
                ('amount_persons', models.IntegerField(verbose_name='Кількість персон')),
                ('order', models.TextField(blank=True, verbose_name='Замовлення')),
                ('special_requests', models.TextField(blank=True, verbose_name='Особливі побажання')),
            ],
        ),
    ]
