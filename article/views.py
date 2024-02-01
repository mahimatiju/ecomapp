from django.shortcuts import render, redirect
from rest_framework import generics

from .models import Article, Article_Category
from .serializers import ArticleSerializer, ArticleCategorySerializer
from .forms import ArticleForm, ArticleCategory


# Create your views here.
class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleCategoryList(generics.ListCreateAPIView):
    queryset = Article_Category.objects.all()
    serializer_class = ArticleCategorySerializer


class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleCategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article_Category.objects.all()
    serializer_class = ArticleCategorySerializer

def demo(request):
    article = Article.objects.all()
    return render(request, "article.html", {"article": article})


def add_article(request):
    form = ArticleForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/')
    form = ArticleForm()
    return render(request, "add_article.html", {"form": form})


def add_category(request):
    form = ArticleCategory(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect("article:add_article")
    form = ArticleCategory()
    return render(request, "article_category.html", {'form': form})
