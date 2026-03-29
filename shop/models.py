from django.db import models


class Category(models.Model):
    type = models.CharField(max_length=200)
    readable_type = models.CharField(max_length=200, null=True, blank=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='subcategories'
    )

    def __str__(self):
        return self.type

    def get_readable_type(self):
        return self.readable_type


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
    has_sizes = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    SIZE_CHOICES = [
        ('XS', 'XS'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('XXXL', 'XXXL'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, 
                                related_name='sizes')
    size = models.CharField(max_length=4, choices=SIZE_CHOICES)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.size}"