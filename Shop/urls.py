# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="Home"),
    path('about/',views.about),
    path('shop/',views.Shop),
    path('contact/',views.Contact),
]
