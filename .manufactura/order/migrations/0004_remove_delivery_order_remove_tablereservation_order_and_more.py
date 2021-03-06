# Generated by Django 4.0.4 on 2022-06-23 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_tablereservation_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='order',
        ),
        migrations.RemoveField(
            model_name='tablereservation',
            name='order',
        ),
        migrations.RemoveField(
            model_name='takeaway',
            name='order',
        ),
        migrations.AddField(
            model_name='delivery',
            name='order_comment',
            field=models.TextField(default='', verbose_name='Коментар до замовлення'),
        ),
        migrations.AddField(
            model_name='tablereservation',
            name='order_comment',
            field=models.TextField(blank=True, default='', verbose_name='Кометнар до замовлення'),
        ),
        migrations.AddField(
            model_name='takeaway',
            name='order_comment',
            field=models.TextField(default='', verbose_name='Коментар до замовлення'),
        ),
    ]
