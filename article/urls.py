from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path("", views.demo, name="demo"),
    path("add_article", views.add_article, name="add_article"),
    path("add_category", views.add_category, name="add_category"),
    path("api_article/", views.ArticleList.as_view()),
    path("apiarticle_category", views.ArticleCategoryList.as_view()),
    path("apiarticle_details/<int:pk>/", views.ArticleDetails.as_view()),
    path("apicategory_details/<int:pk>/", views.ArticleCategoryDetails.as_view()),

]
