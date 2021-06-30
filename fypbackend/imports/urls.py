from django.conf.urls import url, include
from .views import ImportViewSet, ProductViewSet, ExportViewSet, LocalsViewSet, ExportIndentViewSet, \
    ImportIndentViewSet, CustomerExporterListView, CustomerImporterListView, CustomerIndenterListView, CustomerListView, CustomerPartnerListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("imports", ImportViewSet, basename="imports")
router.register("products", ProductViewSet, basename="posts-rates")
router.register("exports", ExportViewSet, basename="exports")
router.register("locals", LocalsViewSet, basename="locals")
router.register("importindents", ImportIndentViewSet, basename="importindents")
router.register("exportindents", ExportIndentViewSet, basename="exportindents")
router.register("customerexporter", CustomerExporterListView, basename="customerexporter")
router.register("customerimporter", CustomerImporterListView, basename="customerimporter")
router.register("customerindenter", CustomerIndenterListView, basename="customerindenter")
router.register("customerpartner", CustomerPartnerListView, basename="customerpartner")
router.register("allcustomers", CustomerListView, basename="allcustomers")

urlpatterns = [
    url('', include(router.urls)),
    # path('customer/<int:id>/', views.CustomerListView.as_view(), name='customer')
]

