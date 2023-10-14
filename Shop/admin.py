from django.contrib import admin
from .models import Categories, Home_Slider, Qoutes, BestSelling
from .models import Sub_Categories
from .models import Products
from .models import Product_Images


# Register your models here.
class CategoryList(admin.ModelAdmin):
    list_display = ('Cateogry_name',)


admin.site.register(Categories, CategoryList)


class SubCatList(admin.ModelAdmin):
    list_display = ("subCategory_name", "Category",)


admin.site.register(Sub_Categories, SubCatList)


class PictureInline(admin.TabularInline):
    model = Product_Images


class ProductList(admin.ModelAdmin):
    list_display = ("product_name", "product_category", "product_subcategory", "product_status",)
    inlines = [PictureInline]


admin.site.register(Products, ProductList)


class SliderList(admin.ModelAdmin):
    list_display = ("slider_heading", "slider_text", "slider_priorty")


admin.site.register(Home_Slider, SliderList)


class QouteList(admin.ModelAdmin):
    list_display = ("qoute", "auther", "forDate")


admin.site.register(Qoutes, QouteList)


class BestSellingList(admin.ModelAdmin):
    list_display = ("Product_id", "product_name", "Added_Dated")

    def product_name(self, obj):
        return obj.Product_id.product_name


admin.site.register(BestSelling, BestSellingList)
