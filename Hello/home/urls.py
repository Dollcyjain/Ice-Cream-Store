from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('buy1', views.buy1, name='buy1'),
    path('buy2', views.buy2, name='buy2'),
    path('buy3', views.buy3, name='buy3'),
    path('buy4', views.buy4, name='buy4'),
    path('buy5', views.buy5, name='buy5'),
    path('buy6', views.buy6, name='buy6'),
    path('buy7', views.buy7, name='buy7'),
    path('buy8', views.buy8, name='buy8'),
]