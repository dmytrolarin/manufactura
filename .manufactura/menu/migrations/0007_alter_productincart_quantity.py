# Generated by Django 4.0.4 on 2022-06-30 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_productincart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productincart',
            name='quantity',
            field=models.IntegerField(verbose_name='Кількість страви'),
        ),
    ]
