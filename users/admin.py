from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = (
        "email",
        "phone_number",
        "date_of_birth",
        "department",
        "is_staff",
        "is_superuser",
    )
    list_filter = ("is_staff", "is_superuser", "department")
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("phone_number", "date_of_birth", "department")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )

    search_fields = ("email", "phone_number")


admin.site.register(User, CustomUserAdmin)
