from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    era = models.CharField(max_length=254, null=True, blank=True)
    diet = models.CharField(max_length=254, null=True, blank=True)
    aggressiveness = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    length = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    star_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
