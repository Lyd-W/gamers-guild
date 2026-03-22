from django.db import models


class Category(models.Model):
    type = models.CharField(max_length=200)
    nice_type = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.type

    def get_nice_type(self):
        return self.nice_type


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=4, decimal_places=1,
                                 null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True,
                              blank=True)
    image_URL = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
