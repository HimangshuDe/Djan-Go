from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from auth_app.models import CustomUserModel

# Register your models here.


@admin.register(CustomUserModel)
class CustomUserAdmin(UserAdmin):
    model = CustomUserModel
    list_display = ("email", "phone_number", "is_staff", "is_active")
    list_filter = ("email", "phone_number", "is_staff", "is_active")
    fieldsets = (  # fieldsets for editing an existing user from admin site.
        (None, {"fields": ("email", "phone_number", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "user_permissions",
                    "groups",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                )
            },
        ),
        (
            "Important dates",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )
    add_fieldsets = (  # fieldsets for adding a new user from admin site.
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "phone_number",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.site_title = "Django Authentication"
admin.site.site_header = "Django Authentication"
