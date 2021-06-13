from django.contrib import admin
from .models import Products, Imports, ShipmentDetails, Exports, Locals, Customer, ImportIndent, ExportIndent

# Register your models here.
admin.site.register(Imports)
admin.site.register(Products)
admin.site.register(ShipmentDetails)
admin.site.register(Exports)
admin.site.register(Locals)
admin.site.register(Customer)
admin.site.register(ImportIndent)
admin.site.register(ExportIndent)
