# Generated by Django 2.2.6 on 2019-11-04 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_foodtype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodtype',
            old_name='typenames',
            new_name='typename',
        ),
    ]
