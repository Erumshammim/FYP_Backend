# Generated by Django 3.0.5 on 2021-07-01 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0007_auto_20210627_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='imports',
            name='priceInKg',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='imports',
            name='totalPrice',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]