import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from .models import Products, BestSelling, Qoutes
from .models import Categories
from .models import Sub_Categories
from .models import Home_Slider

bestProducts = []
def index(request):
    global bestProducts
    featured_products = Products.objects.filter(isFeatured=1).all()
    products_with_images = [(product, product.product_images.first()) for product in featured_products]
    featured_SubCat = Sub_Categories.objects.filter(isFeautred=1).all()
    slider = Home_Slider.objects.exclude(slider_priorty=0).all()
    bestSelling = BestSelling.objects.filter(status=1).values("Product_id")

    bestProducts = [
        (product, product.product_images.first())
        for ids in bestSelling
        for product in Products.objects.filter(id=ids['Product_id'])
    ]
    today = datetime.date.today()
    today = today.strftime('%Y-%m-%d')
    # timezone.now().date()
    qoute = Qoutes.objects.filter(forDate=today).values()
    data = dict(products=products_with_images, subCats=featured_SubCat, slider=slider, bestSeller=bestProducts,
                qoutes=qoute)
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
