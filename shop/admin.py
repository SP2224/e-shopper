from django.contrib import admin

from .models import Product

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'mobile_no', 'address']
    search_fields = ['mobile_no', 'address']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'quantity', 'price', 'offer', 'show_image']
    list_editable = ['quantity', 'price', 'offer']
    search_fields = ['title', 'category']

admin.site.register(Product, ProductAdmin)