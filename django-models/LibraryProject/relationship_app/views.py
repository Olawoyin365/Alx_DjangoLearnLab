from django.shortcuts import render
from django.http import HttpResponse
from .models import Library
from django.views.generic.detail import DetailView


#Function-based view; List all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


#Class-based view; Library detail with its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
