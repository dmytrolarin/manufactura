# Generated by Django 4.0.4 on 2022-07-13 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0021_alter_tablereservation_reason_for_cancel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablereservation',
            name='status',
            field=models.CharField(default='new', max_length=128, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='takeaway',
            name='status',
            field=models.CharField(default='new', max_length=128, verbose_name='Статус'),
        ),
    ]
