# Generated by Django 4.1 on 2022-09-03 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRP', '0002_alter_inform_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inform',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
