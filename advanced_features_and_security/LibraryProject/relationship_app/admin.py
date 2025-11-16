from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.forms import TextInput, Textarea
from django import forms


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # What fields to show in the admin list page
    list_display = (
        "email",
        "date_of_birth",
        "is_staff",
        "is_active",
    )

    # Fieldsets → shown when editing a user
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    # Fields shown when creating a user in admin
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "date_of_birth", "profile_photo"),
            },
        ),
    )

    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
