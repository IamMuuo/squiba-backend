from django.contrib import admin
from django.contrib.admin.filters import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import CustomUser


# Configure how users will display on the admin site
class CustomUserAdmin(admin.ModelAdmin):
    # fields to display
    list_display = (
        "first_name",
        "last_name",
        "email",
        "mobile_phone_number",
        "is_staff",
        "is_active",
        "date_joined",
        "last_login",
        "profile_photo",
    )
    ordering = ("first_name", "last_name", "email")

    # Apply filters
    list_filter = ("is_staff", "is_active")


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
