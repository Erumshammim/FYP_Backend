from rest_framework import serializers
from .models import Products, Imports, Exports, Locals, ImportIndent, ExportIndent, Customer, ShipmentDetails, TestApi


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


# Import serializer
class ImportSerializer(serializers.ModelSerializer):
    shipmentDetails = ShipmentSerializer()

    # priority_choices = serializers.SerializerMethodField()

    def get_priority_choices(self, obj):
        return [choice[0] for choice in Imports.payment_choices]

    class Meta:
        model = Imports
        fields = '__all__'
        # fields = ('id', 'dealDate', 'arrivalDate', 'quantity', 'netWeight', 'productDetails', 'paymentTerm',
        #           'status', 'shipmentDetails', 'exporter', 'partner', 'indenter', 'totalPrice', 'priceInKg')
        depth = 1

    def update(self, instance, validated_data):
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

    # priority_choices = serializers.SerializerMethodField()
    #
    def get_priority_choices(self, obj):
        return [choice[0] for choice in Exports.payment_choices]

    class Meta:
        model = Exports
        fields = '__all__'
        # fields = ('id', 'dealDate', 'departureDate', 'quantity', 'netWeight', 'productDetails', 'paymentTerm',
        #           'status', 'shipmentDetails', 'exporter', 'partner', 'indenter', 'totalPrice', 'priceInKg')
        depth = 1

    def update(self, instance, validated_data):
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

    class Meta:
        model = Locals
        fields = (
            'id', 'dealDate', 'quantity', 'netWeight', 'priceInKg', 'productDetails', 'load', 'condition',
            'paymentTerm',
            'status', 'partner', 'buyer', 'broker', 'totalPrice')
        depth = 1


# importindent serializer
class ImportIndentSerializer(serializers.ModelSerializer):
    shipmentDetails = ShipmentSerializer()

    # priority_choices = serializers.SerializerMethodField()
    #
    def get_priority_choices(self, obj):
        return [choice[0] for choice in ImportIndent.payment_choices]

    class Meta:
        model = ImportIndent
        fields = '__all__'
        depth = 1

    def update(self, instance, validated_data):
        nested_serializer = self.fields['shipmentDetails']
        nested_instance = instance.shipmentDetails
        nested_data = validated_data.pop('shipmentDetails')
        nested_serializer.update(nested_instance, nested_data)
        return super(ImportIndentSerializer, self).update(instance, validated_data)


# exportindent serializer
class ExportIndentSerializer(serializers.ModelSerializer):
    shipmentDetails = ShipmentSerializer()

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
        nested_serializer = self.fields['shipmentDetails']
        nested_instance = instance.shipmentDetails
        nested_data = validated_data.pop('shipmentDetails')
        nested_serializer.update(nested_instance, nested_data)
        return super(ExportIndentSerializer, self).update(instance, validated_data)


# customer serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'customerName', 'customerType')


class TestApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestApi
        fields = '__all__'
