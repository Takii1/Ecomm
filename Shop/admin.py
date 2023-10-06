from django.contrib import admin
from .models import Categories
from .models import Sub_Categories
from .models import Products
from .models import Product_Images


# Register your models here.
class Category_list(admin.ModelAdmin):
    list_display = ('Cateogry_name',)


admin.site.register(Categories, Category_list)


class Sub_cat_List(admin.ModelAdmin):
    list_display = ("subCategory_name", "Category",)


admin.site.register(Sub_Categories, Sub_cat_List)


class PictureInline(admin.TabularInline):
    model = Product_Images


class Product_list(admin.ModelAdmin):
    list_display = ("product_name", "product_category", "product_subcategory", "product_status",)
    inlines = [PictureInline]


admin.site.register(Products, Product_list)
