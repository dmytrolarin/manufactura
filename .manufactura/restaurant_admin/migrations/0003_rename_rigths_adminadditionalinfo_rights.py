# Generated by Django 4.0.4 on 2022-07-08 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_admin', '0002_alter_adminadditionalinfo_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminadditionalinfo',
            old_name='rigths',
            new_name='rights',
        ),
    ]