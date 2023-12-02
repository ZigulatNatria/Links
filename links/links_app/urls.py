from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import BookmarkSerializerAPI, snippet_list, CollectionsSerializerAPI


router = SimpleRouter()
router.register(r'book', BookmarkSerializerAPI, basename='book')
router.register(r'collections', CollectionsSerializerAPI, basename='collections')


urlpatterns = [
    path('api', snippet_list, name='api'),
    path('', include(router.urls)),
]