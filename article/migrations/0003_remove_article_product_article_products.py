# Generated by Django 5.0.1 on 2024-01-16 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0002_article_product"),
        ("ecomapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="article",
            name="product",
        ),
        migrations.AddField(
            model_name="article",
            name="products",
            field=models.ManyToManyField(related_name="articles", to="ecomapp.product"),
        ),
    ]
