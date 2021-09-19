# from django.conf.urls import url
from .views import ImportViewSet, ProductViewSet, ExportViewSet, LocalsViewSet, ExportIndentViewSet, \
    ImportIndentViewSet, CustomerExporterListView, CustomerImporterListView, CustomerIndenterListView, \
    CustomerListView, \
    CustomerPartnerListView, \
    CustomerBuyerListView, CustomerBrokerListView, CustomerSellerListView, ImageApiViewset, \
    account_list, accounts_list_by_contract, account_detail, import_list_by_status, \
    export_list_by_status, local_list_by_status, import_indent_list_by_status, export_indent_list_by_status, \
    bank_account_list, photo_list, photo_list_by_imports, photo_detail, photo_list_exports, photo_detail_exports, \
    photo_list_by_exports, photo_list_by_locals, photo_list_locals, photo_detail_locals, \
    photo_list_by_import_indent, photo_list_import_indent, photo_detail_import_indent, \
    photo_list_by_export_indent, photo_list_export_indent, photo_detail_export_indent


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
    
    #cost sheet urls
    path('accounts/', account_list),
    path('accounts/<slug:slug>/<int:id>/', accounts_list_by_contract),
    path('accounts/<int:id>/', account_detail),
    
    #filtering urls
    path('imports_by_status/', import_list_by_status),
    path('exports_by_status/', export_list_by_status),
    path('locals_by_status/', local_list_by_status),
    path('import_indents_by_status/', import_indent_list_by_status),
    path('export_indents_by_status/', export_indent_list_by_status),

    #Bank Account urls
    path('bank_accounts/', bank_account_list),

    #Photo imports
    path('photos/imports/', photo_list.as_view()),
    path('photos/imports/<int:id>/', photo_list_by_imports),
    path('photo/imports/<int:id>/', photo_detail.as_view()),

    #Photo Exports
    path('photos/exports/', photo_list_exports.as_view()),
    path('photos/exports/<int:id>/', photo_list_by_exports),
    path('photo/exports/<int:id>/', photo_detail_exports.as_view()),

    #Photo Locals
    path('photos/locals/', photo_list_locals.as_view()),
    path('photos/locals/<int:id>/', photo_list_by_locals),
    path('photo/locals/<int:id>/', photo_detail_locals.as_view()),

    #Photo ImportIndent
    path('photos/import_indent/', photo_list_import_indent.as_view()),
    path('photos/import_indent/<int:id>/', photo_list_by_import_indent),
    path('photo/import_indent/<int:id>/', photo_detail_import_indent.as_view()),

    #Photo ExportIndent
    path('photos/export_indent/', photo_list_export_indent.as_view()),
    path('photos/export_indent/<int:id>/', photo_list_by_export_indent),
    path('photo/export_indent/<int:id>/', photo_detail_export_indent.as_view()),
]
urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
