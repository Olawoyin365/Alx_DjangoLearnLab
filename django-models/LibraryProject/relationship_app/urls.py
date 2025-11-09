from django.contrib import path
from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.book_list),
    path('library_detail/', views.LibraryDetailView.as_view()),

]
