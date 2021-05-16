from django.contrib import admin
from django.urls import path
from .views import *
app_name = 'home'

from .views import *
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>', CategoryItemView.as_view(), name='category'),
    path('brand/<name>', BrandView.as_view(), name='brand'),
    path('item_detail/<slug>', ItemDetailView.as_view(), name='item_detail'),
    path('search', ItemSearchView.as_view(), name='search'),
    path('signup', signup, name='signup'),
]
