from django import forms
from .models import Article, Article_Category


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleCategory(forms.ModelForm):
    class Meta:
        model = Article_Category
        fields = '__all__'
