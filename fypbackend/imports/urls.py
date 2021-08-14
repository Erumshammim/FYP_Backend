# from django.conf.urls import url
from .views import ImportViewSet, ProductViewSet, ExportViewSet, LocalsViewSet, ExportIndentViewSet, \
    ImportIndentViewSet, CustomerExporterListView, CustomerImporterListView, CustomerIndenterListView, \
    CustomerListView, \
    CustomerPartnerListView, \
    CustomerBuyerListView, CustomerBrokerListView, CustomerSellerListView, ImageApiViewset, account_list, accounts_list_by_contract, account_detail

from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

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
router.register("customerbroker", CustomerBrokerListView, basename="customerbroker")
router.register("customerbuyer", CustomerBuyerListView, basename="customerbuyer")
router.register("customerseller", CustomerSellerListView, basename="customerseller")
router.register("allcustomers", CustomerListView, basename="allcustomers")
router.register("imageapi", ImageApiViewset, basename="imageapi")

urlpatterns = [
    # url(r'^api/imports/(?P<pk>\d+)/$', UpdateImport.as_view()),
    # url('', include(router.urls)),
    path('accounts/', account_list),
    path('accounts/<slug:slug>/<int:id>/', accounts_list_by_contract),
    path('accounts/<int:id>/', account_detail),
]
urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
