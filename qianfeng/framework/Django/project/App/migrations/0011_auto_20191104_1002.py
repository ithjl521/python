# Generated by Django 2.2.6 on 2019-11-04 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_goods'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='childidname',
            new_name='childcidname',
        ),
    ]
