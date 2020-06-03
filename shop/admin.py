from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *

# Register your models here.
class OurUserAdmin(BaseUserAdmin):
    list_display = [
        'id',
        'name',
        'username',
        'email',
        'mobile_no',
    ]
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password')}),
        ('Personal info', {'fields': ('name', 'mobile_no')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password1', 'password2')}),
        ('Personal info', {'fields': ('name', 'mobile_no')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'name', 'phone')
    ordering = ('email',)
    filter_horizontal = ()

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'category',
        'sub_category',
        'category_type',
        'usable_by',
        'quantity',
    ]

admin.site.register(OurUser, OurUserAdmin)
admin.site.register(Product, ProductAdmin)