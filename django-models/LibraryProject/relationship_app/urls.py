from django.contrib import path
from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('book_list/', views.book_list),
    path('library_detail/', views.LibraryDetailView.as_view()),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html')),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html')),
    path('register/', views.register),

]
