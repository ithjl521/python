# Generated by Django 2.2.6 on 2019-10-29 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Three', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_num', models.CharField(max_length=16, unique=True)),
                ('o_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
