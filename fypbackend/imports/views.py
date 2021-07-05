from django.db.models import F
from django.shortcuts import render
from .serializers import ImportSerializer, ProductSerializer, ExportSerializer, \
    LocalSerializer, ImportIndentSerializer, \
    ExportIndentSerializer, CustomerSerializer
from .models import Imports, Products, Exports, Locals, ImportIndent, ExportIndent, Customer, ShipmentDetails
from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.
# API for Import module
class ImportViewSet(viewsets.ModelViewSet):
    serializer_class = ImportSerializer

    def get_queryset(self):
        posts = Imports.objects.all()
        return posts

    def create(self, request, *args, **kwargs):
        post_data = request.data

        # new_rate = Products.objects.create(
        #     productName=post_data["productDetails"]["productName"])
        # new_rate.save()
        product_data = Products.objects.get(id=post_data["productDetails"])

        new_shipment = ShipmentDetails.objects.create(
            blNo=post_data["shipmentDetails"]["blNo"],
            shipDate=post_data["shipmentDetails"]["shipDate"],
            vesselName=post_data["shipmentDetails"]["vesselName"],
            vesselType=post_data["shipmentDetails"]["vesselType"],
            load=post_data["shipmentDetails"]["load"])
        new_shipment.save()

        exporters = Customer.objects.get(id=post_data["exporter"])
        partners = Customer.objects.get(id=post_data["partner"])
        indenters = Customer.objects.get(id=post_data["indenter"])
        # data = Customer.objects.filter(id=post_data["exporter"])
        # post_data['exporter'] = [1, 2, 3]
        # qs1 = Imports.objects.filter().values('quantity', 'priceInKg').aggregate(Sum(F('quantity') * F('priceInKg')))
        result = Imports.objects.filter(quantity__gt=F('quantity') + F('priceInKg'))
        new_post = Imports.objects.create(
            dealDate=post_data["dealDate"], arrivalDate=post_data["arrivalDate"],
            quantity=post_data["quantity"], netWeight=post_data["netWeight"],
            paymentTerm=post_data["paymentTerm"], status=post_data["status"],
            shipmentDetails=new_shipment, exporter=exporters, partner=partners, indenter=indenters,
            productDetails=product_data, priceInKg=post_data["priceInKg"], totalPrice=result)

        new_post.save()

        # new_post.__dict__
        #
        # new_post.print()
        serializer = ImportSerializer(new_post)

        return Response(serializer.data)

    # def get(self, request, *args, **kwargs):
    #
    #     try:
    #         id = request.query_params["id"]
    #         if id != None:
    #             imports = Imports.objects.get(id=id)
    #             # imports.__dict__
    #             print(imports.__dict__)
    #
    #             serializer = ImportSerializer(imports)
    #     except:
    #         imports = self.get_queryset()
    #         serializer = ImportSerializer(imports, many=True)
    #
    #     return Response(serializer.data)
    def put(self, request, *args, **kwargs):
        id = request.query_params["id"]
        import_object = Imports.objects.get(id=id)

        data = request.data

        import_object.dealDate = data["dealDate"]
        import_object.arrivalDate = data["arrivalDate"]
        import_object.quantity = data["quantity"]
        import_object.netWeight = data["netWeight"]
        import_object.paymentTerm = data[" paymentTerm"]
        import_object.status = data[" status"]
        import_object.productDetails = data[" productDetails"]
        import_object.shipmentDetails = data[" shipmentDetails"]
        import_object.exporter = data["exporter"]
        import_object.partner = data["partner"]
        import_object.indenter = data["indenter"]
        import_object.save()
        serializer = ImportSerializer(import_object)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        import_object = Imports.objects.get()
        data = request.data

        import_object.dealDate = data.get("dealDate", import_object.dealDate)
        import_object.arrivalDate = data.get("arrivalDate", import_object.arrivalDate)
        import_object.quantity = data.get("quantity", import_object.quantity)
        import_object.netWeight = data.get("netWeight", import_object.netWeight)
        import_object.paymentTerm = data.get("paymentTerm", import_object.paymentTerm)
        import_object.status = data.get("status", import_object.status)
        import_object.productDetails = data.get("productDetails", import_object.productDetails)
        import_object.shipmentDetails = data.get("shipmentDetails", import_object.shipmentDetails)
        import_object.exporter = data.get("exporter", import_object.exporter)
        import_object.partner = data.get("partner", import_object.partner)
        import_object.indenter = data.get("indenter", import_object.indenter)

        import_object.save()
        serializer = ImportSerializer(import_object)

        return Response(serializer.data)


# function to get customer type of exporter
class CustomerExporterListView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        expotercustomers = Customer.objects.filter(customerType__startswith='exporter').values()
        return expotercustomers


# function to get customer type of importer
class CustomerImporterListView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        importercustomers = Customer.objects.filter(customerType__startswith='importer').values()
        return importercustomers


# function to get customer type of indenter
class CustomerIndenterListView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        indentercustomers = Customer.objects.filter(customerType__startswith='indenter').values()
        return indentercustomers


# function to get customer of type partner
class CustomerPartnerListView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        partnercustomers = Customer.objects.filter(customerType__startswith='partner').values()
        return partnercustomers


# function to get customer of type broker
class CustomerBrokerListView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        brokercustomers = Customer.objects.filter(customerType__startswith='broker').values()
        return brokercustomers


# function to get customer of type buyer
class CustomerBuyerListView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        buyercustomers = Customer.objects.filter(customerType__startswith='buyer').values()
        return buyercustomers


# function to get customer of type seller
class CustomerSellerListView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        sellercustomers = Customer.objects.filter(customerType__startswith='seller').values()
        return sellercustomers


# function to get all customers
class CustomerListView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        customers = Customer.objects.all()
        return customers


# API to get all products
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        rates = Products.objects.all()
        return rates


# API for export module
class ExportViewSet(viewsets.ModelViewSet):
    serializer_class = ExportSerializer

    def get_queryset(self):
        posts = Exports.objects.all()
        return posts

    def create(self, request, *args, **kwargs):
        post_data = request.data
        product_data = Products.objects.get(id=post_data["productDetails"])
        new_shipment = ShipmentDetails.objects.create(
            blNo=post_data["shipmentDetails"]["blNo"],
            shipDate=post_data["shipmentDetails"]["shipDate"],
            vesselName=post_data["shipmentDetails"]["vesselName"],
            vesselType=post_data["shipmentDetails"]["vesselType"],
            load=post_data["shipmentDetails"]["load"])
        new_shipment.save()
        exporters = Customer.objects.get(id=post_data["exporter"])
        partners = Customer.objects.get(id=post_data["partner"])
        indenters = Customer.objects.get(id=post_data["indenter"])
        totalcalc = Exports.objects.filter(quantity__gt=F('quantity') + F('priceInKg'))
        new_post = Exports.objects.create(
            dealDate=post_data["dealDate"], departureDate=post_data["departureDate"],
            quantity=post_data["quantity"], netWeight=post_data["netWeight"],
            paymentTerm=post_data["paymentTerm"], status=post_data["status"],
            shipmentDetails=new_shipment, exporter=exporters, partner=partners, indenter=indenters,
            productDetails=product_data, totalPrice=totalcalc, priceInKg=post_data["priceInKg"])
        new_post.save()
        serializer = ExportSerializer(new_post)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        id = request.query_params["id"]
        export_object = Exports.objects.get(id=id)

        data = request.data

        export_object.dealDate = data["dealDate"]
        export_object.departureDate = data["departureDate"]
        export_object.quantity = data["quantity"]
        export_object.netWeight = data["netWeight"]
        export_object.price = data["price"]
        export_object.paymentTerm = data[" paymentTerm"]
        export_object.status = data[" status"]
        export_object.productDetails = data[" productDetails"]
        export_object.shipmentDetails = data[" shipmentDetails"]
        export_object.save()
        serializer = ExportSerializer(export_object)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        export_object = Exports.objects.get()
        data = request.data

        export_object.dealDate = data.get("dealDate", export_object.dealDate)
        export_object.departureDate = data.get("departureDate", export_object.departureDate)
        export_object.quantity = data.get("quantity", export_object.quantity)
        export_object.netWeight = data.get("netWeight", export_object.netWeight)
        export_object.price = data.get("price", export_object.price)
        export_object.paymentTerm = data.get("paymentTerm", export_object.paymentTerm)
        export_object.status = data.get("status", export_object.status)
        export_object.productDetails = data.get("productDetails", export_object.productDetails)
        export_object.shipmentDetails = data.get("shipmentDetails", export_object.shipmentDetails)

        export_object.save()
        serializer = ExportSerializer(export_object)

        return Response(serializer.data)


# API for locals module
class LocalsViewSet(viewsets.ModelViewSet):
    serializer_class = LocalSerializer

    def get_queryset(self):
        posts = Locals.objects.all()
        return posts

    def create(self, request, *args, **kwargs):
        post_data = request.data

        product_data = Products.objects.get(id=post_data["productDetails"])
        partners = Customer.objects.get(id=post_data["partner"])
        buyers = Customer.objects.get(id=post_data["buyer"])
        brokers = Customer.objects.get(id=post_data["broker"])
        totalcalc = Locals.objects.filter(quantity__gt=F('quantity') + F('priceInKg'))

        new_post = Locals.objects.create(
            dealDate=post_data["dealDate"], quantity=post_data["quantity"], netWeight=post_data["netWeight"],
            priceInKg=post_data["priceInKg"], paymentTerm=post_data["paymentTerm"], status=post_data["status"],
            load=post_data["load"], condition=post_data["condition"], productDetails=product_data, partner=partners,
            buyer=buyers, broker=brokers, totalPrice=totalcalc)
        new_post.save()
        serializer = LocalSerializer(new_post)

        return Response(serializer.data)

    def get(self, request, *args, **kwargs):

        try:
            id = request.query_params["id"]
            if id != None:
                local = Locals.objects.get(id=id)
                serializer = LocalSerializer(local)
        except:
            local = self.get_queryset()
            serializer = LocalSerializer(local, many=True)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        id = request.query_params["id"]
        locals_object = Locals.objects.get(id=id)

        data = request.data

        locals_object.dealDate = data["dealDate"]
        locals_object.quantity = data["quantity"]
        locals_object.netWeight = data["netWeight"]
        locals_object.price = data["price"]
        locals_object.paymentTerm = data[" paymentTerm"]
        locals_object.status = data[" status"]
        locals_object.productDetails = data[" productDetails"]
        locals_object.load = data[" load"]
        locals_object.condition = data[" condition"]
        locals_object.save()
        serializer = LocalSerializer(locals_object)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        locals_object = Locals.objects.get()
        data = request.data

        locals_object.dealDate = data.get("dealDate", locals_object.dealDate)
        locals_object.quantity = data.get("quantity", locals_object.quantity)
        locals_object.netWeight = data.get("netWeight", locals_object.netWeight)
        locals_object.price = data.get("price", locals_object.price)
        locals_object.paymentTerm = data.get("paymentTerm", locals_object.paymentTerm)
        locals_object.status = data.get("status", locals_object.status)
        locals_object.productDetails = data.get("productDetails", locals_object.productDetails)
        locals_object.load = data.get("load", locals_object.load)
        locals_object.condition = data.get("condition", locals_object.condition)

        locals_object.save()
        serializer = LocalSerializer(locals_object)

        return Response(serializer.data)


# API for exportindent module
class ExportIndentViewSet(viewsets.ModelViewSet):
    serializer_class = ExportIndentSerializer

    def get_queryset(self):
        posts = ExportIndent.objects.all()
        return posts

    def create(self, request, *args, **kwargs):
        post_data = request.data

        product_data = Products.objects.get(id=post_data["productDetails"])
        new_shipment = ShipmentDetails.objects.create(
            blNo=post_data["shipmentDetails"]["blNo"],
            shipDate=post_data["shipmentDetails"]["shipDate"],
            vesselName=post_data["shipmentDetails"]["vesselName"],
            vesselType=post_data["shipmentDetails"]["vesselType"],
            load=post_data["shipmentDetails"]["load"])
        new_shipment.save()
        partners = Customer.objects.get(id=post_data["partner"])
        buyers = Customer.objects.get(id=post_data["buyer"])
        sellers = Customer.objects.get(id=post_data["seller"])
        totalcalc = ExportIndent.objects.filter(quantity__gt=F('quantity') + F('priceInKg'))

        new_post = ExportIndent.objects.create(
            dealDate=post_data["dealDate"], arrivalDate=post_data["arrivalDate"],
            departureDate=post_data["departureDate"],
            quantity=post_data["quantity"], netWeight=post_data["netWeight"], priceInKg=post_data["priceInKg"],
            paymentTerm=post_data["paymentTerm"], indentCommission=post_data["indentCommission"],
            shipmentDetails=new_shipment, productDetails=product_data,
            partner=partners, buyer=buyers, seller=sellers, totalPrice=totalcalc)
        new_post.save()
        serializer = ExportIndentSerializer(new_post)

        return Response(serializer.data)

    def get(self, request, *args, **kwargs):

        try:
            id = request.query_params["id"]
            if id != None:
                exporter = ExportIndent.objects.get(id=id)
                serializer = ExportIndentSerializer(exporter)
        except:
            exporter = self.get_queryset()
            serializer = ExportIndentSerializer(exporter, many=True)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        id = request.query_params["id"]
        exportindent_object = ExportIndent.objects.get(id=id)

        data = request.data

        exportindent_object.dealDate = data["dealDate"]
        exportindent_object.arrivalDate = data["arrivalDate"]
        exportindent_object.departureDate = data["departureDate"]
        exportindent_object.quantity = data["quantity"]
        exportindent_object.netWeight = data["netWeight"]
        exportindent_object.price = data["price"]
        exportindent_object.paymentTerm = data[" paymentTerm"]
        exportindent_object.indentCommission = data[" indentCommission"]
        exportindent_object.productDetails = data[" productDetails"]
        exportindent_object.shipmentDetails = data[" shipmentDetails"]
        exportindent_object.save()
        serializer = ExportIndentSerializer(exportindent_object)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        exportindent_object = ExportIndent.objects.get()
        data = request.data

        exportindent_object.dealDate = data.get("dealDate", exportindent_object.dealDate)
        exportindent_object.arrivalDate = data.get("arrivalDate", exportindent_object.arrivalDate)
        exportindent_object.departureDate = data.get("departureDate", exportindent_object.departureDate)
        exportindent_object.quantity = data.get("quantity", exportindent_object.quantity)
        exportindent_object.netWeight = data.get("netWeight", exportindent_object.netWeight)
        exportindent_object.price = data.get("price", exportindent_object.price)
        exportindent_object.paymentTerm = data.get("paymentTerm", exportindent_object.paymentTerm)
        exportindent_object.indentCommission = data.get("indentCommission", exportindent_object.indentCommission)
        exportindent_object.productDetails = data.get("productDetails", exportindent_object.productDetails)
        exportindent_object.shipmentDetails = data.get("shipmentDetails", exportindent_object.shipmentDetails)

        exportindent_object.save()
        serializer = ExportIndentSerializer(exportindent_object)

        return Response(serializer.data)


# API for importindent module
class ImportIndentViewSet(viewsets.ModelViewSet):
    serializer_class = ImportIndentSerializer

    def get_queryset(self):
        posts = ImportIndent.objects.all()
        return posts

    def create(self, request, *args, **kwargs):
        post_data = request.data

        product_data = Products.objects.get(id=post_data["productDetails"])
        new_shipment = ShipmentDetails.objects.create(
            blNo=post_data["shipmentDetails"]["blNo"],
            shipDate=post_data["shipmentDetails"]["shipDate"],
            vesselName=post_data["shipmentDetails"]["vesselName"],
            vesselType=post_data["shipmentDetails"]["vesselType"],
            load=post_data["shipmentDetails"]["load"])
        new_shipment.save()
        partners = Customer.objects.get(id=post_data["partner"])
        buyers = Customer.objects.get(id=post_data["buyer"])
        sellers = Customer.objects.get(id=post_data["seller"])
        totalcalc = ImportIndent.objects.filter(quantity__gt=F('quantity') + F('priceInKg'))

        new_post = ImportIndent.objects.create(
            dealDate=post_data["dealDate"], arrivalDate=post_data["arrivalDate"],
            departureDate=post_data["departureDate"],
            quantity=post_data["quantity"], netWeight=post_data["netWeight"], priceInKg=post_data["priceInKg"],
            paymentTerm=post_data["paymentTerm"], indentCommission=post_data["indentCommission"],
            shipmentDetails=new_shipment, productDetails=product_data,
            partner=partners, buyer=buyers, seller=sellers, totalPrice=totalcalc)
        new_post.save()
        serializer = ImportIndentSerializer(new_post)

        return Response(serializer.data)

    def get(self, request, *args, **kwargs):

        try:
            id = request.query_params["id"]
            if id != None:
                importer = ImportIndent.objects.get(id=id)
                serializer = ImportIndentSerializer(importer)
        except:
            importer = self.get_queryset()
            serializer = ImportIndentSerializer(importer, many=True)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        id = request.query_params["id"]
        importindent_object = ImportIndent.objects.get(id=id)

        data = request.data

        importindent_object.dealDate = data["dealDate"]
        importindent_object.arrivalDate = data["arrivalDate"]
        importindent_object.quantity = data["quantity"]
        importindent_object.netWeight = data["netWeight"]
        importindent_object.price = data["price"]
        importindent_object.paymentTerm = data[" paymentTerm"]
        importindent_object.indentCommission = data[" indentCommission"]
        importindent_object.productDetails = data[" productDetails"]
        importindent_object.shipmentDetails = data[" shipmentDetails"]
        importindent_object.save()
        serializer = ImportIndentSerializer(importindent_object)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        importindent_object = ImportIndent.objects.get()
        data = request.data

        importindent_object.dealDate = data.get("dealDate", importindent_object.dealDate)
        importindent_object.arrivalDate = data.get("arrivalDate", importindent_object.arrivalDate)
        importindent_object.quantity = data.get("quantity", importindent_object.quantity)
        importindent_object.netWeight = data.get("netWeight", importindent_object.netWeight)
        importindent_object.price = data.get("price", importindent_object.price)
        importindent_object.paymentTerm = data.get("paymentTerm", importindent_object.paymentTerm)
        importindent_object.indentCommission = data.get("indentCommission", importindent_object.indentCommission)
        importindent_object.productDetails = data.get("productDetails", importindent_object.productDetails)
        importindent_object.shipmentDetails = data.get("shipmentDetails", importindent_object.shipmentDetails)

        importindent_object.save()
        serializer = ImportIndentSerializer(importindent_object)
        return Response(serializer.data)
