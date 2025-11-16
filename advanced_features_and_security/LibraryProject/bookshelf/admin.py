from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from django.contrib import admin
from .models import Book, CustomUser

# Register your models here.
# @admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'date_of_birth', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active', 'date_joined', 'date_of_birth']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal Info', {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'date_of_birth',
                'profile_photo'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_year']
    list_filter = ['publication_year', 'author']
    search_fields = ['title', 'author']

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    if sender.name != "accounts" and sender.name != "your_app_name":
        return  # avoid running for irrelevant apps

    # Get Book model permissions
    content_type = ContentType.objects.get_for_model(Book)

    can_view = Permission.objects.get(codename="can_view", content_type=content_type)
    can_create = Permission.objects.get(codename="can_create", content_type=content_type)
    can_edit = Permission.objects.get(codename="can_edit", content_type=content_type)
    can_delete = Permission.objects.get(codename="can_delete", content_type=content_type)

    # Create groups
    editors, created = Group.objects.get_or_create(name="Editors")
    viewers, created = Group.objects.get_or_create(name="Viewers")
    admins, created = Group.objects.get_or_create(name="Admins")

    # Assign permissions
    viewers.permissions.set([can_view])

    editors.permissions.set([can_view, can_create, can_edit])

    admins.permissions.set([
        can_view, can_create, can_edit, can_delete
    ])
