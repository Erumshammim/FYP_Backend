# Generated by Django 3.0.5 on 2021-08-13 06:14

from django.db import migrations, models
import django.db.models.deletion
import imports.models


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
            name='Image',
            fields=[
                ('contractId', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, default='', upload_to=imports.models.upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=200)),
                ('priceInKg', models.IntegerField(default=0)),
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
                ('priceInKg', models.PositiveIntegerField(default=0)),
                ('load', models.FloatField()),
                ('condition', models.CharField(max_length=100)),
                ('paymentTerm', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card')], default='Cash', max_length=4)),
                ('status', models.CharField(choices=[('Signed', 'Signed'), ('Unsigned', 'Unsigned'), ('Pending', 'Pending')], default='Signed', max_length=9)),
                ('totalPrice', models.PositiveIntegerField(blank=True, null=True)),
                ('broker', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='broker', to='imports.Customer')),
                ('buyer', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='imports.Customer')),
                ('partner', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='localpartner', to='imports.Customer')),
                ('productDetails', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.Products')),
            ],
        ),
        migrations.CreateModel(
            name='Imports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealDate', models.DateField()),
                ('arrivalDate', models.DateField()),
                ('quantity', models.PositiveIntegerField()),
                ('netWeight', models.FloatField()),
                ('priceInKg', models.PositiveIntegerField(default=0)),
                ('paymentTerm', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card')], default='Cash', max_length=4)),
                ('status', models.CharField(choices=[('Signed', 'Signed'), ('Unsigned', 'Unsigned'), ('Pending', 'Pending')], default='Signed', max_length=9)),
                ('totalPrice', models.PositiveIntegerField(blank=True, null=True)),
                ('exporter', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exporters', to='imports.Customer')),
                ('indenter', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='indenters', to='imports.Customer')),
                ('partner', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partners', to='imports.Customer')),
                ('productDetails', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.Products')),
                ('shipmentDetails', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.ShipmentDetails')),
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
                ('priceInKg', models.PositiveIntegerField(default=0)),
                ('paymentTerm', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card')], default='Cash', max_length=4)),
                ('status', models.CharField(choices=[('Signed', 'Signed'), ('Unsigned', 'Unsigned'), ('Pending', 'Pending')], default='Signed', max_length=9)),
                ('indentCommission', models.IntegerField()),
                ('totalPrice', models.PositiveIntegerField(blank=True, null=True)),
                ('buyer', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyers', to='imports.Customer')),
                ('partner', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='importindentpartner', to='imports.Customer')),
                ('productDetails', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.Products')),
                ('seller', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='imports.Customer')),
                ('shipmentDetails', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.ShipmentDetails')),
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
                ('priceInKg', models.PositiveIntegerField(default=0)),
                ('paymentTerm', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card')], default='Cash', max_length=4)),
                ('status', models.CharField(choices=[('Signed', 'Signed'), ('Unsigned', 'Unsigned'), ('Pending', 'Pending')], default='Signed', max_length=9)),
                ('totalPrice', models.PositiveIntegerField(blank=True, null=True)),
                ('exporter', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exporterss', to='imports.Customer')),
                ('indenter', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='indenterss', to='imports.Customer')),
                ('partner', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partnerss', to='imports.Customer')),
                ('productDetails', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.Products')),
                ('shipmentDetails', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.ShipmentDetails')),
            ],
        ),
        migrations.CreateModel(
            name='ExportIndent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealDate', models.DateField()),
                ('departureDate', models.DateField()),
                ('quantity', models.IntegerField()),
                ('netWeight', models.FloatField()),
                ('priceInKg', models.PositiveIntegerField(default=0)),
                ('paymentTerm', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card')], default='Cash', max_length=4)),
                ('status', models.CharField(choices=[('Signed', 'Signed'), ('Unsigned', 'Unsigned'), ('Pending', 'Pending')], default='Signed', max_length=9)),
                ('indentCommission', models.IntegerField()),
                ('totalPrice', models.PositiveIntegerField(blank=True, null=True)),
                ('buyer', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exportindentbuyer', to='imports.Customer')),
                ('partner', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exportindentpartner', to='imports.Customer')),
                ('productDetails', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.Products')),
                ('seller', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exportindentseller', to='imports.Customer')),
                ('shipmentDetails', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.ShipmentDetails')),
            ],
        ),
    ]
