# Generated by Django 3.2.3 on 2021-05-29 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=100)),
                ('customerType', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blNo', models.CharField(max_length=100)),
                ('shipDate', models.DateField()),
                ('vesselName', models.CharField(max_length=70)),
                ('vesselType', models.CharField(max_length=70)),
                ('load', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Locals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealDate', models.DateField()),
                ('quantity', models.IntegerField()),
                ('netWeight', models.FloatField()),
                ('price', models.IntegerField()),
                ('load', models.FloatField()),
                ('condition', models.CharField(max_length=100)),
                ('paymentTerm', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card')], default='Cash', max_length=4)),
                ('status', models.CharField(choices=[('Signed', 'Signed'), ('Unsigned', 'Unsigned'), ('Pending', 'Pending')], default='Signed', max_length=9)),
                ('productDetails', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.products')),
            ],
        ),
        migrations.CreateModel(
            name='Imports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealDate', models.DateField()),
                ('arrivalDate', models.DateField()),
                ('quantity', models.IntegerField()),
                ('netWeight', models.FloatField()),
                ('price', models.IntegerField()),
                ('paymentTerm', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card')], default='Cash', max_length=4)),
                ('status', models.CharField(choices=[('Signed', 'Signed'), ('Unsigned', 'Unsigned'), ('Pending', 'Pending')], default='Signed', max_length=9)),
                ('exporter', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.customer')),
                ('productDetails', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.products')),
                ('shipmentDetails', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.shipmentdetails')),
            ],
        ),
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
                ('productDetails', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.products')),
                ('shipmentDetails', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.shipmentdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Exports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealDate', models.DateField()),
                ('departureDate', models.DateField()),
                ('quantity', models.IntegerField()),
                ('netWeight', models.FloatField()),
                ('price', models.IntegerField()),
                ('paymentTerm', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card')], default='Cash', max_length=4)),
                ('status', models.CharField(choices=[('Signed', 'Signed'), ('Unsigned', 'Unsigned'), ('Pending', 'Pending')], default='Signed', max_length=9)),
                ('productDetails', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.products')),
                ('shipmentDetails', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.shipmentdetails')),
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
                ('productDetails', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.products')),
                ('shipmentDetails', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.shipmentdetails')),
            ],
        ),
    ]
