from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User


class CustomUserAdmin(UserAdmin):
    
    # Add first_name and last_name to the displayed columns
    list_display = ('email', 'first_name', 'last_name',
                    'phone_number', 'is_staff', 'is_active', 'last_login')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'phone_number', 'first_name', 'last_name')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {
         'fields': ('first_name', 'last_name', 'phone_number')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone_number', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )


admin.site.register(User, CustomUserAdmin)
