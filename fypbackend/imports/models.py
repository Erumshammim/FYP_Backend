from django.db import models
from datetime import datetime


# Create your models here.


class Products(models.Model):
    productName = models.CharField(max_length=200)
    priceInKg = models.IntegerField(default=0)

    def __str__(self):
        return self.productName


class ShipmentDetails(models.Model):
    blNo = models.CharField(max_length=100)
    shipDate = models.DateField()
    vesselName = models.CharField(max_length=70)
    vesselType = models.CharField(max_length=70)
    load = models.FloatField()

    def __str__(self):
        return self.blNo


class Customer(models.Model):
    customerName = models.CharField(max_length=100)
    customerType = models.CharField(max_length=100)

    def __str__(self):
        return self.customerName


# this is imports model
class Imports(models.Model):
    payment_choices = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
    ]
    status_choices = [
        ('Signed', 'Signed'),
        ('Unsigned', 'Unsigned'),
        ('Pending', 'Pending'),
    ]
    dealDate = models.DateField()
    arrivalDate = models.DateField()
    quantity = models.PositiveIntegerField()
    netWeight = models.FloatField()
    priceInKg = models.PositiveIntegerField(default=0)
    productDetails = models.ForeignKey(
        Products, on_delete=models.CASCADE, null=True, default='')
    paymentTerm = models.CharField(max_length=4, choices=payment_choices, default='Cash')
    status = models.CharField(max_length=9, choices=status_choices, default='Signed')
    shipmentDetails = models.OneToOneField(
        ShipmentDetails, on_delete=models.CASCADE, null=True, default='')
    exporter = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='exporters', null=True, default='')
    partner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='partners', null=True, default='')
    indenter = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='indenters', null=True, default='')
    totalPrice = models.PositiveIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.totalPrice = self.priceInKg * self.quantity
        super(Imports, self).save(*args, **kwargs)


class Exports(models.Model):
    payment_choices = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
    ]
    status_choices = [
        ('Signed', 'Signed'),
        ('Unsigned', 'Unsigned'),
        ('Pending', 'Pending'),
    ]
    dealDate = models.DateField()
    departureDate = models.DateField()
    quantity = models.IntegerField()
    netWeight = models.FloatField()
    priceInKg = models.PositiveIntegerField(default=0)
    paymentTerm = models.CharField(max_length=4, choices=payment_choices, default='Cash')
    status = models.CharField(max_length=9, choices=status_choices, default='Signed')
    productDetails = models.ForeignKey(
        Products, on_delete=models.CASCADE, null=True, default='')
    shipmentDetails = models.OneToOneField(
        ShipmentDetails, on_delete=models.CASCADE, null=True, default='')
    exporter = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='exporterss', null=True, default='')
    partner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='partnerss', null=True, default='')
    indenter = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='indenterss', null=True, default='')
    totalPrice = models.PositiveIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.totalPrice = self.priceInKg * self.quantity
        super(Exports, self).save(*args, **kwargs)


class Locals(models.Model):
    payment_choices = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
    ]
    status_choices = [
        ('Signed', 'Signed'),
        ('Unsigned', 'Unsigned'),
        ('Pending', 'Pending'),
    ]
    dealDate = models.DateField()
    quantity = models.IntegerField()
    netWeight = models.FloatField()
    priceInKg = models.PositiveIntegerField(default=0)
    productDetails = models.ForeignKey(
        Products, on_delete=models.CASCADE, null=True, default='')
    load = models.FloatField()
    condition = models.CharField(max_length=100)
    paymentTerm = models.CharField(max_length=4, choices=payment_choices, default='Cash')
    status = models.CharField(max_length=9, choices=status_choices, default='Signed')
    partner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='localpartner', null=True, default='')
    buyer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='buyer', null=True, default='')
    broker = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='broker', null=True, default='')
    totalPrice = models.PositiveIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.totalPrice = self.priceInKg * self.quantity
        super(Locals, self).save(*args, **kwargs)


# this is import indent table
class ImportIndent(models.Model):
    payment_choices = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
    ]
    dealDate = models.DateField()
    arrivalDate = models.DateField()
    departureDate = models.DateField(default=datetime.now)
    quantity = models.IntegerField()
    netWeight = models.FloatField()
    priceInKg = models.PositiveIntegerField(default=0)
    productDetails = models.ForeignKey(
        Products, on_delete=models.CASCADE, null=True, default='')
    paymentTerm = models.CharField(max_length=4, choices=payment_choices, default='Cash')
    indentCommission = models.IntegerField()
    shipmentDetails = models.OneToOneField(
        ShipmentDetails, on_delete=models.CASCADE, null=True, default='')
    partner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='importindentpartner', null=True,
                                default='')
    buyer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='buyers', null=True, default='')
    seller = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='seller', null=True, default='')
    totalPrice = models.PositiveIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.totalPrice = self.priceInKg * self.quantity
        super(ImportIndent, self).save(*args, **kwargs)


# this is export indent table
class ExportIndent(models.Model):
    payment_choices = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
    ]
    dealDate = models.DateField()
    arrivalDate = models.DateField()
    departureDate = models.DateField()
    quantity = models.IntegerField()
    netWeight = models.FloatField()
    priceInKg = models.PositiveIntegerField(default=0)
    productDetails = models.ForeignKey(
        Products, on_delete=models.CASCADE, null=True, default='')
    paymentTerm = models.CharField(max_length=4, choices=payment_choices, default='Cash')
    indentCommission = models.IntegerField()
    shipmentDetails = models.OneToOneField(
        ShipmentDetails, on_delete=models.CASCADE, null=True, default='')
    partner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='exportindentpartner', null=True,
                                default='')
    buyer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='exportindentbuyer', null=True,
                              default='')
    seller = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='exportindentseller', null=True,
                               default='')
    totalPrice = models.PositiveIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.totalPrice = self.priceInKg * self.quantity
        super(ExportIndent, self).save(*args, **kwargs)
