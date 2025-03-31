from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена: ')
    have = models.BooleanField(default=True, verbose_name='v nalichii')
    description = models.TextField()
    video = models.ImageField(upload_to='product_videos/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_photos/', null=True, blank=True)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product_name}, {self.price}'
