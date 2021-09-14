from rest_framework import serializers
from .models import Products, Imports, Exports, Locals, ImportIndent, ExportIndent, Customer, ShipmentDetails, Image, Account, BackAccount, Photo


# shipment Serializer
class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentDetails
        fields = ('id', 'blNo', 'shipDate', 'vesselName', 'vesselType', 'load')


# Product serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

# customer serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'customerName', 'customerType')

# Import serializer
class ImportSerializer(serializers.ModelSerializer):
    shipmentDetails = ShipmentSerializer()
    productId = serializers.IntegerField(write_only=True)
    exporterId = serializers.IntegerField(write_only=True)
    indenterId = serializers.IntegerField(write_only=True)
    partnerId = serializers.IntegerField(write_only=True)
    productDetails = ProductSerializer(read_only=True)
    exporter = CustomerSerializer(read_only=True)
    partner = CustomerSerializer(read_only=True)
    indenter = CustomerSerializer(read_only=True)

    # priority_choices = serializers.SerializerMethodField()

    def get_priority_choices(self, obj):
        return [choice[0] for choice in Imports.payment_choices]

    class Meta:
        model = Imports
        #fields = '__all__'
        fields = ('id', 'productId', 'exporterId', 'partnerId', 'indenterId', 'dealDate', 'arrivalDate', 'quantity', 'netWeight', 'productDetails', 'paymentTerm',
                   'status', 'shipmentDetails', 'exporter', 'partner', 'indenter', 'totalPrice', 'priceInKg')
        depth = 1

    def update(self, instance, validated_data):
        productId = validated_data.pop('productId')
        exporterId = validated_data.pop('exporterId')
        partnerId = validated_data.pop('partnerId')
        indenterId = validated_data.pop('indenterId')
        instance.productDetails = Products.objects.get(id=productId)
        instance.exporter = Customer.objects.get(id=exporterId)
        instance.partner = Customer.objects.get(id=partnerId)
        instance.indenter = Customer.objects.get(id=indenterId)
        nested_serializer = self.fields['shipmentDetails']
        nested_instance = instance.shipmentDetails
        nested_data = validated_data.pop('shipmentDetails')
        nested_serializer.update(nested_instance, nested_data)
        return super(ImportSerializer, self).update(instance, validated_data)

    # def update(self, instance, validated_data):
    #     person_data = validated_data.get('productDetails')
    #     instance.productDetails.id = person_data.get(
    #         'id',
    #         instance.productDetails.id
    #     )
    #     instance.productDetails.save()
    #     return instance


# export serializer
class ExportSerializer(serializers.ModelSerializer):
    shipmentDetails = ShipmentSerializer()
    productId = serializers.IntegerField(write_only=True)
    exporterId = serializers.IntegerField(write_only=True)
    indenterId = serializers.IntegerField(write_only=True)
    partnerId = serializers.IntegerField(write_only=True)
    productDetails = ProductSerializer(read_only=True)
    exporter = CustomerSerializer(read_only=True)
    partner = CustomerSerializer(read_only=True)
    indenter = CustomerSerializer(read_only=True)

    # priority_choices = serializers.SerializerMethodField()
    #
    def get_priority_choices(self, obj):
        return [choice[0] for choice in Exports.payment_choices]

    class Meta:
        model = Exports
        fields = '__all__'
        fields = ('id', 'productId', 'exporterId', 'partnerId', 'indenterId', 'dealDate', 'departureDate', 'quantity', 'netWeight', 'productDetails', 'paymentTerm',
                   'status', 'shipmentDetails', 'exporter', 'partner', 'indenter', 'totalPrice', 'priceInKg')
        depth = 1

    def update(self, instance, validated_data):
        productId = validated_data.pop('productId')
        exporterId = validated_data.pop('exporterId')
        partnerId = validated_data.pop('partnerId')
        indenterId = validated_data.pop('indenterId')
        instance.productDetails = Products.objects.get(id=productId)
        instance.exporter = Customer.objects.get(id=exporterId)
        instance.partner = Customer.objects.get(id=partnerId)
        instance.indenter = Customer.objects.get(id=indenterId)
        nested_serializer = self.fields['shipmentDetails']
        nested_instance = instance.shipmentDetails
        nested_data = validated_data.pop('shipmentDetails')
        nested_serializer.update(nested_instance, nested_data)
        return super(ExportSerializer, self).update(instance, validated_data)


# local serializer
class LocalSerializer(serializers.ModelSerializer):
    # priority_choices = serializers.SerializerMethodField()
    #
    def get_priority_choices(self, obj):
        return [choice[0] for choice in Locals.payment_choices]

    productId = serializers.IntegerField(write_only=True)
    partnerId = serializers.IntegerField(write_only=True)
    brokerId = serializers.IntegerField(write_only=True)
    buyerId = serializers.IntegerField(write_only=True)
    productDetails = ProductSerializer(read_only=True)
    partner = CustomerSerializer(read_only=True)
    broker = CustomerSerializer(read_only=True)
    buyer = CustomerSerializer(read_only=True)

    class Meta:
        model = Locals
        fields = (
            'id', 'productId', 'partnerId', 'brokerId', 'buyerId', 'dealDate', 'quantity', 'netWeight', 'priceInKg', 'productDetails', 'load', 'condition',
            'paymentTerm',
            'status', 'partner', 'buyer', 'broker', 'totalPrice')
        depth = 1

    def update(self, instance, validated_data):
        productId = validated_data.pop('productId')
        brokerId = validated_data.pop('brokerId')
        partnerId = validated_data.pop('partnerId')
        buyerId = validated_data.pop('buyerId')
        instance.productDetails = Products.objects.get(id=productId)
        instance.broker = Customer.objects.get(id=brokerId)
        instance.partner = Customer.objects.get(id=partnerId)
        instance.buyer = Customer.objects.get(id=buyerId)
        return super(LocalSerializer, self).update(instance, validated_data)

# importindent serializer
class ImportIndentSerializer(serializers.ModelSerializer):
    shipmentDetails = ShipmentSerializer()
    productId = serializers.IntegerField(write_only=True)
    partnerId = serializers.IntegerField(write_only=True)
    sellerId = serializers.IntegerField(write_only=True)
    buyerId = serializers.IntegerField(write_only=True)
    productDetails = ProductSerializer(read_only=True)
    partner = CustomerSerializer(read_only=True)
    seller = CustomerSerializer(read_only=True)
    buyer = CustomerSerializer(read_only=True)

    # priority_choices = serializers.SerializerMethodField()
    #
    def get_priority_choices(self, obj):
        return [choice[0] for choice in ImportIndent.payment_choices]

    class Meta:
        model = ImportIndent
        fields = '__all__'
        depth = 1

    def update(self, instance, validated_data):
        productId = validated_data.pop('productId')
        sellerId = validated_data.pop('sellerId')
        partnerId = validated_data.pop('partnerId')
        buyerId = validated_data.pop('buyerId')
        instance.productDetails = Products.objects.get(id=productId)
        instance.seller = Customer.objects.get(id=sellerId)
        instance.partner = Customer.objects.get(id=partnerId)
        instance.buyer = Customer.objects.get(id=buyerId)
        nested_serializer = self.fields['shipmentDetails']
        nested_instance = instance.shipmentDetails
        nested_data = validated_data.pop('shipmentDetails')
        nested_serializer.update(nested_instance, nested_data)
        return super(ImportIndentSerializer, self).update(instance, validated_data)


# exportindent serializer
class ExportIndentSerializer(serializers.ModelSerializer):
    shipmentDetails = ShipmentSerializer()
    productId = serializers.IntegerField(write_only=True)
    partnerId = serializers.IntegerField(write_only=True)
    sellerId = serializers.IntegerField(write_only=True)
    buyerId = serializers.IntegerField(write_only=True)
    productDetails = ProductSerializer(read_only=True)
    partner = CustomerSerializer(read_only=True)
    seller = CustomerSerializer(read_only=True)
    buyer = CustomerSerializer(read_only=True)

    # priority_choices = serializers.SerializerMethodField()

    def get_priority_choices(self, obj):
        return [choice[0] for choice in ExportIndent.payment_choices]

    class Meta:
        model = ExportIndent
        fields = '__all__'
        # fields = ('id', 'dealDate', 'arrivalDate', 'departureDate', 'quantity', 'netWeight', 'priceInKg',
        #           'productDetails', 'paymentTerm',
        #           'indentCommission', 'shipmentDetails', 'partner', 'buyer', 'seller', 'totalPrice')
        depth = 1

    def update(self, instance, validated_data):
        productId = validated_data.pop('productId')
        sellerId = validated_data.pop('sellerId')
        partnerId = validated_data.pop('partnerId')
        buyerId = validated_data.pop('buyerId')
        instance.productDetails = Products.objects.get(id=productId)
        instance.seller = Customer.objects.get(id=sellerId)
        instance.partner = Customer.objects.get(id=partnerId)
        instance.buyer = Customer.objects.get(id=buyerId)
        nested_serializer = self.fields['shipmentDetails']
        nested_instance = instance.shipmentDetails
        nested_data = validated_data.pop('shipmentDetails')
        nested_serializer.update(nested_instance, nested_data)
        return super(ExportIndentSerializer, self).update(instance, validated_data)


#BankAccount Serializer
class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackAccount
        fields = '__all__'


# Account Serializer
class AccountSerializer(serializers.HyperlinkedModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.IntegerField(write_only=True, required=False)
    back_account = BankAccountSerializer(read_only=True)
    back_account_id = serializers.IntegerField(write_only=True, required=False)


    class Meta:
        model = Account
        fields = ['id', 'date', 'particulars', 'debit', 'credit', 'balance', 'customer_id', 'customer', 
                    'contract_id', 'contract_type', 'back_account', 'back_account_id']

# image api
class ImageApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    #imports = ImportSerializer(read_only=True)
    imports_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Photo
        fields = ['id', 'photo', 'imports_id']