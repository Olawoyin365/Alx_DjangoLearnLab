from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

@permission_required('your_app_name.can_view', raise_exception=True)
def book_list(request):
    pass

@permission_required('your_app_name.can_create', raise_exception=True)
def create_book(request):
    pass


@permission_required('your_app_name.can_edit', raise_exception=True)
def edit_book(request, pk):
    pass


@permission_required('your_app_name.can_delete', raise_exception=True)
def delete_book(request, pk):
    pass
# Create your views here.
