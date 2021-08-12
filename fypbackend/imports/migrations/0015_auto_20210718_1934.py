# Generated by Django 3.0.5 on 2021-07-18 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0014_auto_20210716_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='exportindent',
            name='status',
            field=models.CharField(choices=[('Signed', 'Signed'), ('Unsigned', 'Unsigned'), ('Pending', 'Pending')], default='Signed', max_length=9),
        ),
        migrations.AddField(
            model_name='importindent',
            name='status',
            field=models.CharField(choices=[('Signed', 'Signed'), ('Unsigned', 'Unsigned'), ('Pending', 'Pending')], default='Signed', max_length=9),
        ),
    ]