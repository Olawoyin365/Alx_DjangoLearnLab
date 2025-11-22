from django.urls import path
from resr_framework.routers import DefaultRouter
from .views import BookList


router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]
