from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from customuser_app.models import CustomUserModel


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Field Heading',
            {
                'fields': (
                    'displayname',
                ),
            },
        ),
    )


admin.site.register(CustomUserModel, CustomUserAdmin)
