from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.parsers import MultiPartParser

from .models import Product, Category
from .forms import ProductForm, CategoryForm
from rest_framework import generics
from .serializers import CustomerSerializer, CategorySerializer


# Create your views here.
def list(request):
    list = Product.objects.all()
    return render(request, "product_list.html", {"list": list})


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CustomerSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = CustomerSerializer


class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

def product(request, id):
    pro = Product.objects.get(id=id)
    return render(request, "product.html", {"pro": pro})


def category(request):
    cat = Category.objects.all()
    return render(request, "category.html", {"cat": cat})


def p_category(request, id):
    p_cat = Category.objects.get(id=id)
    category_p = Product.objects.filter(category=p_cat)
    return render(request, "pcategory.html", {"pcat": p_cat, "category": category_p})


def add_product(request):
    form = ProductForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/')
    form = ProductForm()

    return render(request, 'add_product.html', {'form': form})


def add_category(request):
    form = CategoryForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect("ecomapp:add_product")
    form = CategoryForm()
    return render(request, "add_category.html", {'form': form})
