from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')  # Add related_name
    price = models.IntegerField()
    Image = models.ImageField(upload_to="pic")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
