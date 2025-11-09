from django.shortcuts import render
from django.http import HttpResponse
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test


#Function-based view; List all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


#Class-based view; Library detail with its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def log_in(request):
    return render(request, 'relationship_app/login.html')

def log_out(request):
    return render(request, 'relationship_app/logout.html')

def register(request):
    UserCreationForm()
    return render(request, 'relationship_app/register.html')

#Helper functions to check user roles
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


#Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


#Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


#Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
