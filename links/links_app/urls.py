from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import index, BookmarkSerializerAPI, snippet_list


router = SimpleRouter()
router.register(r'book', BookmarkSerializerAPI, basename='book')
# router.register(r'book_add', snippet_list, basename='book_add')


urlpatterns = [
    path('save', index, name='index'),
    path('api', snippet_list, name='api'),
    path('', include(router.urls)),
]