from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Product


class ProductAdmin(SummernoteModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )
    summernote_fields = ('description',)


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
