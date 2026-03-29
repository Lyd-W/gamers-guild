from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Product, ProductSize


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1


class ProductAdmin(SummernoteModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )
    summernote_fields = ('description',)
    inlines = [ProductSizeInline]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
