from django.urls import path
from . import views

app_name = "ecomapp"

urlpatterns = [
    path("", views.list, name="list"),
    path("apiproducts/", views.ProductList.as_view()),
    path("apicategory/", views.CategoryList.as_view()),
    path("apiproduct_details/<int:pk>/", views.ProductDetails.as_view()),
    path("apicategory_details/<int:pk>/", views.CategoryDetails.as_view()),
    path("product/<int:id>/", views.product, name="product"),
    path("category", views.category, name="category"),
    path("p_category/<int:id>/", views.p_category, name="p_category"),
    path("add", views.add_product, name="add_product"),
    path("add_category", views.add_category, name="add_category"),

]
