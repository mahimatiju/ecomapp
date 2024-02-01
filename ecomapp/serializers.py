from rest_framework import serializers

from article.models import Article, Article_Category
from .models import Product, Category


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price', 'Image']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']


