from rest_framework import serializers
from .models import Products, Imports, Exports, Locals, ImportIndent, ExportIndent, Customer


# Import serializer
class ImportSerializer(serializers.ModelSerializer):
    # priority_choices = serializers.SerializerMethodField()
    #
    def get_priority_choices(self, obj):
        return [choice[0] for choice in Imports.payment_choices]

    class Meta:
        model = Imports
        fields = ('id', 'dealDate', 'arrivalDate', 'quantity', 'netWeight', 'productDetails', 'paymentTerm',
                  'status', 'shipmentDetails', 'exporter', 'partner', 'indenter')
        depth = 1


class ExportSerializer(serializers.ModelSerializer):
    # priority_choices = serializers.SerializerMethodField()
    #
    def get_priority_choices(self, obj):
        return [choice[0] for choice in Exports.payment_choices]

    class Meta:
        model = Exports
        fields = ('id', 'dealDate', 'departureDate', 'quantity', 'netWeight', 'productDetails', 'paymentTerm',
                  'status', 'shipmentDetails', 'exporter', 'partner', 'indenter')
        depth = 1


class LocalSerializer(serializers.ModelSerializer):
    # priority_choices = serializers.SerializerMethodField()
    #
    def get_priority_choices(self, obj):
        return [choice[0] for choice in Locals.payment_choices]

    class Meta:
        model = Locals
        fields = (
            'id', 'dealDate', 'quantity', 'netWeight', 'price', 'productDetails', 'load', 'condition', 'paymentTerm',
            'status')
        depth = 1


class ImportIndentSerializer(serializers.ModelSerializer):
    # priority_choices = serializers.SerializerMethodField()
    #
    def get_priority_choices(self, obj):
        return [choice[0] for choice in ImportIndent.payment_choices]

    class Meta:
        model = ImportIndent
        fields = ('id', 'dealDate', 'arrivalDate', 'quantity', 'netWeight', 'price', 'productDetails', 'paymentTerm',
                  'indentCommission', 'shipmentDetails')
        depth = 1


class ExportIndentSerializer(serializers.ModelSerializer):
    # priority_choices = serializers.SerializerMethodField()
    #
    def get_priority_choices(self, obj):
        return [choice[0] for choice in ExportIndent.payment_choices]

    class Meta:
        model = ExportIndent
        fields = ('id', 'dealDate', 'arrivalDate', 'departureDate', 'quantity', 'netWeight', 'price', 'productDetails',
                  'paymentTerm',
                  'indentCommission', 'shipmentDetails')
        depth = 1


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'customerName', 'customerType')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
