# Generated by Django 3.0.5 on 2021-05-01 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0007_locals'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportIndent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealDate', models.DateField()),
                ('arrivalDate', models.DateField()),
                ('quantity', models.IntegerField()),
                ('netWeight', models.FloatField()),
                ('price', models.IntegerField()),
                ('paymentTerm', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card')], default='Cash', max_length=4)),
                ('indentCommission', models.IntegerField()),
                ('productDetails', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.Products')),
                ('shipmentDetails', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.ShipmentDetails')),
            ],
        ),
        migrations.CreateModel(
            name='ExportIndent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealDate', models.DateField()),
                ('arrivalDate', models.DateField()),
                ('departureDate', models.DateField()),
                ('quantity', models.IntegerField()),
                ('netWeight', models.FloatField()),
                ('price', models.IntegerField()),
                ('paymentTerm', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card')], default='Cash', max_length=4)),
                ('indentCommission', models.IntegerField()),
                ('productDetails', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.Products')),
                ('shipmentDetails', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.ShipmentDetails')),
            ],
        ),
    ]
