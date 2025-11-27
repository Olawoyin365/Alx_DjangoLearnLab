from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Set of generic views for the Book model that handles CRUD operations.

class BookList(ListAPIView):
    query_set = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetail(RetrieveAPIView):
    query_set = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreate(CreateAPIView):
    query_set = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdate(UpdateAPIView):
    query_set = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDelete(DestroyAPIView):
    query_set = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
