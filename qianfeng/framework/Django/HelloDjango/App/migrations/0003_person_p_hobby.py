# Generated by Django 2.2.6 on 2019-10-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='p_hobby',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
