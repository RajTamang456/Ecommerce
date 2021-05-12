from django.contrib import admin
from django.urls import path
from .views import *
app_name = 'home'

from .views import *
urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('category/<slug>', CategoryItemView.as_view(), name = 'category'),
]
