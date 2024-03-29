# Generated by Django 5.0.1 on 2024-01-16 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0003_remove_article_product_article_products"),
        ("ecomapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="products",
            field=models.ManyToManyField(
                blank=True, related_name="articles", to="ecomapp.product"
            ),
        ),
    ]
