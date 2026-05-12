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

    def get_fields(self, request, obj=None):

        fields = [
            'category',
            'sku',
            'name',
            'description',
            'price',
            'image',
            'image_URL',
            'has_sizes',
        ]

        if obj and not obj.has_sizes:
            fields.append('stock')

        if obj is None:
            fields.append('stock')

        return fields

    def get_inline_instances(self, request, obj=None):

        if obj and obj.has_sizes:
            return [
                inline(self.model, self.admin_site)
                for inline in self.inlines
            ]

        return []


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
