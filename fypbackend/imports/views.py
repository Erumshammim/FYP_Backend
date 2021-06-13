from django.shortcuts import render
from .serializers import ImportSerializer, ProductSerializer, ExportSerializer, \
    LocalSerializer, ImportIndentSerializer, \
    ExportIndentSerializer
from .models import Imports, Products, Exports, Locals, ImportIndent, ExportIndent
from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.
class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = ImportSerializer

    def get_queryset(self):
        posts = Imports.objects.all()
        return posts

    def create(self, request, *args, **kwargs):
        post_data = request.data

        new_rate = Products.objects.create(
            productName=post_data["productDetails"]["productName"])
        new_rate.save()

        new_post = Imports.objects.create(
            dealDate=post_data["dealDate"], arrivalDate=post_data["arrivalDate"],
            quantity=post_data["quantity"], netWeight=post_data["netWeight"], price=post_data["price"],
            choices=post_data["choices"], paymentTerm=post_data["paymentTerm"], status=post_data["status"],
            shipmentDetails=post_data["shipmentDetails"], exporter=post_data["exporter"], productDetails=new_rate)
        new_post.save()
        serializer = ImportSerializer(new_post)

        return Response(serializer.data)

    def get(self, request, *args, **kwargs):

        try:
            id = request.query_params["id"]
            if id != None:
                imports = Imports.objects.get(id=id)
                serializer = ImportSerializer(imports)
        except:
            imports = self.get_queryset()
            serializer = ImportSerializer(imports, many=True)

        return Response(serializer.data)


class PostsRatesViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        rates = Products.objects.all()
        return rates


class ExportViewSet(viewsets.ModelViewSet):
    serializer_class = ExportSerializer

    def get_queryset(self):
        posts = Exports.objects.all()
        return posts

    def create(self, request, *args, **kwargs):
        post_data = request.data

        new_rate = Products.objects.create(
            productName=post_data["productDetails"]["productName"])
        new_rate.save()

        new_post = Exports.objects.create(
            dealDate=post_data["dealDate"], departureDate=post_data["departureDate"],
            quantity=post_data["quantity"], netWeight=post_data["netWeight"], price=post_data["price"],
            choices=post_data["choices"], paymentTerm=post_data["paymentTerm"], status=post_data["status"],
            shipmentDetails=post_data["shipmentDetails"], productDetails=new_rate)
        new_post.save()
        serializer = ExportSerializer(new_post)

        return Response(serializer.data)

    def get(self, request, *args, **kwargs):

        try:
            id = request.query_params["id"]
            if id != None:
                exports = Exports.objects.get(id=id)
                serializer = ExportSerializer(exports)
        except:
            exports = self.get_queryset()
            serializer = ExportSerializer(exports, many=True)

        return Response(serializer.data)


class LocalsViewSet(viewsets.ModelViewSet):
    serializer_class = LocalSerializer

    def get_queryset(self):
        posts = Locals.objects.all()
        return posts

    def create(self, request, *args, **kwargs):
        post_data = request.data

        new_rate = Products.objects.create(
            productName=post_data["productDetails"]["productName"])
        new_rate.save()

        new_post = Locals.objects.create(
            dealDate=post_data["dealDate"], quantity=post_data["quantity"], netWeight=post_data["netWeight"],
            price=post_data["price"],
            choices=post_data["choices"], paymentTerm=post_data["paymentTerm"], status=post_data["status"],
            load=post_data["load"], condition=post_data["condition"], productDetails=new_rate)
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


class ExportIndentViewSet(viewsets.ModelViewSet):
    serializer_class = ExportIndentSerializer

    def get_queryset(self):
        posts = ExportIndent.objects.all()
        return posts

    def create(self, request, *args, **kwargs):
        post_data = request.data

        new_rate = Products.objects.create(
            productName=post_data["productDetails"]["productName"])
        new_rate.save()

        new_post = ExportIndent.objects.create(
            dealDate=post_data["dealDate"], arrivalDate=post_data["arrivalDate"],
            departureDate=post_data["departureDate"],
            quantity=post_data["quantity"], netWeight=post_data["netWeight"], price=post_data["price"],
            choices=post_data["choices"], paymentTerm=post_data["paymentTerm"],
            indentCommission=post_data["indentCommission"],
            shipmentDetails=post_data["shipmentDetails"], productDetails=new_rate)
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


class ImportIndentViewSet(viewsets.ModelViewSet):
    serializer_class = ImportIndentSerializer

    def get_queryset(self):
        posts = ImportIndent.objects.all()
        return posts

    def create(self, request, *args, **kwargs):
        post_data = request.data

        new_rate = Products.objects.create(
            productName=post_data["productDetails"]["productName"])
        new_rate.save()

        new_post = ImportIndent.objects.create(
            dealDate=post_data["dealDate"], arrivalDate=post_data["arrivalDate"],
            quantity=post_data["quantity"], netWeight=post_data["netWeight"], price=post_data["price"],
            choices=post_data["choices"], paymentTerm=post_data["paymentTerm"],
            indentCommission=post_data["indentCommission"],
            shipmentDetails=post_data["shipmentDetails"], productDetails=new_rate)
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
