from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Role

@admin.register(Role)
class RoleAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("role",)}),
    )
    list_display = ("username", "email", "role", "is_staff")

# Register your models here.
