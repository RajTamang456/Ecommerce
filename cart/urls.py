from django.urls import path
from .views import *
app_name = 'cart'
urlpatterns = [
    path('add_to_cart/<slug>', add_to_cart, name='add_to_cart'),
]