
from django.urls import path, include


app_name = 'store'

from .import views

urlpatterns = [

    path('', views.store, name ='store'),
    path('cart/', views.cart, name ='cart'),
    path('checkout/', views.checkout, name ='checkout'),



]
