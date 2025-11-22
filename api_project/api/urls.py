from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
urlspatterns = router.urls


'''urlpatterns = [
    #path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]'''

urlpatterns = [
        path('api/token/', obtain_auth_token),

]
