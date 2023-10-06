from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Products,Product_Images
from .models import Categories
from .models import Sub_Categories


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


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
