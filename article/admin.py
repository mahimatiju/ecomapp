from django.contrib import admin
from . models import Article,Article_Category

# Register your models here.
admin.site.register(Article)
admin.site.register(Article_Category)