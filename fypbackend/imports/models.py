from django.db import models


# Create your models here.
class Products(models.Model):
    productName = models.CharField(max_length=200)

    def __str__(self):
        return self.productName


class ShipmentDetails(models.Model):
    blNo = models.CharField(max_length=100)
    shipDate = models.DateField()
    vesselName = models.CharField(max_length=70)
    vesselType = models.CharField(max_length=70)
    load = models.FloatField()


class Customer(models.Model):
    customerName = models.CharField(max_length=100)
    customerType = models.CharField(max_length=100)


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
    quantity = models.IntegerField()
    netWeight = models.FloatField()
    price = models.IntegerField()
    productDetails = models.OneToOneField(
        Products, on_delete=models.CASCADE, null=True, default='')
    paymentTerm = models.CharField(max_length=4, choices=payment_choices, default='Cash')
    status = models.CharField(max_length=9, choices=status_choices, default='Signed')
    shipmentDetails = models.OneToOneField(
        ShipmentDetails, on_delete=models.CASCADE, null=True, default='')
    exporter = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, default='')


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
    price = models.IntegerField()
    paymentTerm = models.CharField(max_length=4, choices=payment_choices, default='Cash')
    status = models.CharField(max_length=9, choices=status_choices, default='Signed')
    productDetails = models.OneToOneField(
        Products, on_delete=models.CASCADE, null=True, default='')
    shipmentDetails = models.OneToOneField(
        ShipmentDetails, on_delete=models.CASCADE, null=True, default='')


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
    price = models.IntegerField()
    productDetails = models.OneToOneField(
        Products, on_delete=models.CASCADE, null=True, default='')
    load = models.FloatField()
    condition = models.CharField(max_length=100)
    paymentTerm = models.CharField(max_length=4, choices=payment_choices, default='Cash')
    status = models.CharField(max_length=9, choices=status_choices, default='Signed')


class ImportIndent(models.Model):
    payment_choices = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
    ]
    dealDate = models.DateField()
    arrivalDate = models.DateField()
    quantity = models.IntegerField()
    netWeight = models.FloatField()
    price = models.IntegerField()
    productDetails = models.OneToOneField(
        Products, on_delete=models.CASCADE, null=True, default='')
    paymentTerm = models.CharField(max_length=4, choices=payment_choices, default='Cash')
    indentCommission = models.IntegerField()
    shipmentDetails = models.OneToOneField(
        ShipmentDetails, on_delete=models.CASCADE, null=True, default='')


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
    price = models.IntegerField()
    productDetails = models.OneToOneField(
        Products, on_delete=models.CASCADE, null=True, default='')
    paymentTerm = models.CharField(max_length=4, choices=payment_choices, default='Cash')
    indentCommission = models.IntegerField()
    shipmentDetails = models.OneToOneField(
        ShipmentDetails, on_delete=models.CASCADE, null=True, default='')
