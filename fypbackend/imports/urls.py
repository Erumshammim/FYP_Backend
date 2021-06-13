from django.conf.urls import url, include
from .views import PostsViewSet, PostsRatesViewSet, ExportViewSet, LocalsViewSet, ExportIndentViewSet,\
    ImportIndentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("posts", PostsViewSet, basename="posts")
router.register("posts-rates", PostsRatesViewSet, basename="posts-rates")
router.register("exports", ExportViewSet, basename="exports")
router.register("locals", LocalsViewSet, basename="locals")
router.register("importindents", ImportIndentViewSet, basename="importindents")
router.register("exportindents", ExportIndentViewSet, basename="exportindents")


urlpatterns = [
    url('', include(router.urls))
]
