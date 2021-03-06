# Generated by Django 4.0.4 on 2022-06-30 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_delete_tablereservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=128, verbose_name='Код клієнта')),
                ('name', models.CharField(max_length=255, verbose_name='Страва')),
                ('quantity', models.ImageField(upload_to='', verbose_name='Кількість страви')),
            ],
            options={
                'verbose_name': 'Страва в замовленнях',
                'verbose_name_plural': 'Страви в замовленнях',
            },
        ),
    ]
