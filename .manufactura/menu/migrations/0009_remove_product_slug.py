# Generated by Django 4.0.4 on 2022-07-26 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_alter_product_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
