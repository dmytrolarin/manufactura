# Generated by Django 4.0.4 on 2022-06-23 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_delivery_order_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='order_comment',
            field=models.TextField(default='', verbose_name='Коментар до замовлення'),
        ),
        migrations.AlterField(
            model_name='tablereservation',
            name='order_comment',
            field=models.TextField(blank=True, verbose_name='Кометнар до замовлення'),
        ),
        migrations.AlterField(
            model_name='takeaway',
            name='order_comment',
            field=models.TextField(default='', verbose_name='Коментар до замовлення'),
        ),
    ]
