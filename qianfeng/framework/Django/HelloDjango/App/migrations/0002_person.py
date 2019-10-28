# Generated by Django 2.2.6 on 2019-10-28 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=16, unique=True)),
                ('p_age', models.IntegerField(db_column='age', default=18)),
                ('p_sex', models.BooleanField(db_column='sex', default=False)),
            ],
            options={
                'db_table': 'People',
            },
        ),
    ]
