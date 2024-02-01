from django.db import models

# Create your models here.
from ecomapp.models import Product


class Article_Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=500)
    category = models.ForeignKey(Article_Category, on_delete=models.CASCADE, related_name="article_category")
    # product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="article", null=True, blank=True)
    products = models.ManyToManyField(Product, related_name="articles",blank=True)


    def __str__(self):
        return self.title
