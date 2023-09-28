from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def Shop(request):
    template = loader.get_template('shop.html')
    return HttpResponse(template.render())

def Contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())
