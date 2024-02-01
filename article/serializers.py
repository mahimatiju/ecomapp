from rest_framework import serializers

from .models import Article,Article_Category


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'category', 'products']


class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Article_Category
        fields = ['id', 'name']
