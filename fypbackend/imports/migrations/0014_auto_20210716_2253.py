# Generated by Django 3.0.5 on 2021-07-16 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0013_auto_20210705_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exportindent',
            name='arrivalDate',
        ),
        migrations.RemoveField(
            model_name='importindent',
            name='departureDate',
        ),
    ]
