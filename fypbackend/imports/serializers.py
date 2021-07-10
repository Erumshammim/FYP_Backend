from rest_framework import serializers
from .models import Products, Imports, Exports, Locals, ImportIndent, ExportIndent, Customer, ShipmentDetails


# shipment Serializer
class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentDetails
        fields = ('id', 'blNo', 'shipDate', 'vesselName', 'vesselType', 'load')


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


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'customerName', 'customerType')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
