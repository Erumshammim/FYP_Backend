# Generated by Django 3.0.5 on 2021-07-05 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0009_auto_20210702_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locals',
            name='price',
        ),
        migrations.AddField(
            model_name='locals',
            name='broker',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='broker', to='imports.Customer'),
        ),
        migrations.AddField(
            model_name='locals',
            name='buyer',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='imports.Customer'),
        ),
        migrations.AddField(
            model_name='locals',
            name='partner',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='localpartner', to='imports.Customer'),
        ),
        migrations.AddField(
            model_name='locals',
            name='priceInKg',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='locals',
            name='totalPrice',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]