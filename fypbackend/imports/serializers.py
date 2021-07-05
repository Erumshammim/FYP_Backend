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
    #
    def get_priority_choices(self, obj):
        return [choice[0] for choice in Imports.payment_choices]

    class Meta:
        model = Imports
        fields = ('id', 'dealDate', 'arrivalDate', 'quantity', 'netWeight', 'productDetails', 'paymentTerm',
                  'status', 'shipmentDetails', 'exporter', 'partner', 'indenter', 'totalPrice', 'priceInKg')
        depth = 1

    # def update(self, instance, validated_data):
    #     if validated_data.get("shipmentDetails"):
    #         shipmentDetails = validated_data.pop('shipmentDetails')
    #         shipmentDetails = ShipmentDetails.objects.get(id=self.initial_data["shipmentDetails"]["id"])
    #         scene_task = super(ImportSerializer, self, ).update(instance, validated_data)
    #         scene_task.scene = shipmentDetails
    #         scene_task.save()
    #         return scene_task
    #     return super(ImportSerializer, self, ).update(instance, validated_data)


class ExportSerializer(serializers.ModelSerializer):
    # priority_choices = serializers.SerializerMethodField()
    #
    def get_priority_choices(self, obj):
        return [choice[0] for choice in Exports.payment_choices]

    class Meta:
        model = Exports
        fields = ('id', 'dealDate', 'departureDate', 'quantity', 'netWeight', 'productDetails', 'paymentTerm',
                  'status', 'shipmentDetails', 'exporter', 'partner', 'indenter', 'totalPrice', 'priceInKg')
        depth = 1


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
    # priority_choices = serializers.SerializerMethodField()
    #
    def get_priority_choices(self, obj):
        return [choice[0] for choice in ImportIndent.payment_choices]

    class Meta:
        model = ImportIndent
        fields = ('id', 'dealDate', 'arrivalDate', 'departureDate', 'quantity', 'netWeight', 'priceInKg',
                  'productDetails', 'paymentTerm',
                  'indentCommission', 'shipmentDetails', 'partner', 'buyer', 'seller', 'totalPrice')
        depth = 1


class ExportIndentSerializer(serializers.ModelSerializer):
    # priority_choices = serializers.SerializerMethodField()
    #
    def get_priority_choices(self, obj):
        return [choice[0] for choice in ExportIndent.payment_choices]

    class Meta:
        model = ExportIndent
        fields = ('id', 'dealDate', 'arrivalDate', 'departureDate', 'quantity', 'netWeight', 'priceInKg',
                  'productDetails', 'paymentTerm',
                  'indentCommission', 'shipmentDetails', 'partner', 'buyer', 'seller', 'totalPrice')
        depth = 1


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'customerName', 'customerType')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
