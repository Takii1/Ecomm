# from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="Home"),
    path('about/', views.about),
    path('shop/', views.shop),
    path('contact/', views.contact),
    path('shop/<slug:slug>', views.singleProduct, name='details')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
