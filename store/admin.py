from django.contrib import admin

# Register your models here.
from .models import Category, Product

# This automatically populates the slug field based on the name you type
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'is_available', 'created', 'updated']
    list_filter = ['is_available', 'created', 'updated', 'category']
    list_editable = ['price', 'stock', 'is_available']  # Lets you edit straight from the list view
    prepopulated_fields = {'slug': ('name',)}