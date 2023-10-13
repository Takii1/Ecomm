from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Products
from .models import Categories
from .models import Sub_Categories
from .models import Home_Slider


def index(request):
    featured_products = Products.objects.filter(isFeatured=1).all()
    products_with_images = [(product, product.product_images.first()) for product in featured_products]
    featured_SubCat = Sub_Categories.objects.filter(isFeautred=1).all()
    slider = Home_Slider.objects.exclude(slider_priorty=0).all()
    data = {
        "products": products_with_images,
        "subCats": featured_SubCat,
        "slider": slider
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(data, request))


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())


def shop(request):
    products = Products.objects.all()
    products_with_images = [(product, product.product_images.first()) for product in products]
    # categories = Categories.objects.all().values()
    # sub_cat = Sub_Categories.objects.all().values()
    data = {
        "products": products_with_images,
        # "categories": categories,
        # "subCategories": sub_cat,
    }
    template = loader.get_template('shop.html')
    return HttpResponse(template.render(data, request))


def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())
