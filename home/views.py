from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login

from .models import *


# Create your views here.
class BaseView(View):
    views = {}
    views['category'] = Category.objects.filter(status='active')

class HomeView(BaseView):
    def get(self, request):
        self.views['sliders'] = Slider.objects.filter(status='active')
        self.views['ads'] = Ad.objects.all()
        self.views['brands'] = Brand.objects.filter(status='active')
        self.views['hots'] = Item.objects.filter(status='active', label='hot')
        self.views['news'] = Item.objects.filter(status='active', label='new')

        return render(request, 'index.html', self.views)

class CategoryItemView(BaseView):
    def get(self, request, slug):
        category_id = Category.objects.get(slug=slug).id
        self.views['cat_items'] = Item.objects.filter(category=category_id)
        return render(request, 'category.html', self.views)

class BrandView(BaseView):
    def get(self, request, slug):
        brand_id = Brand.objects.get(slug=slug).id
        self.views['brand_items'] = Item.objects.filter(brand=brand_id)
        return render(request, 'brand.html', self.views)

class ItemSearchView(BaseView):
    def get(self, request):
        search = request.GET.get('search', None)
        if search is None:
            return redirect('/')
        else:
            self.views['search_item'] = Item.objects.filter(name__icontains = search)
            return render(request, 'search.html', self.views)

        return render(request, 'search.html')

class ItemDetailView(BaseView):
    def get(self, request, slug):
        self.views['items_details'] = Item.objects.filter(slug=slug)
        return render(request, 'product-list.html', self.views)

def signup(request):
    if request.method == "POST":
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        Cpassword = request.POST['cpassword']
        if password == Cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already taken')
                return redirect('home:signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'This email is already taken')
                return redirect('home:signup')
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=f_name,
                    last_name=l_name,
                )
                user.save()
                messages.success(request, 'You are successfully registered')
                return redirect('home:signup')
        else:
            messages.error(request, 'The password does not match')
            return redirect('home:signup')
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.error(request, 'wrong username and password')
            return redirect('home:login')
    return render(request, 'login.html')


# ______________________________________________________API____________________________________________

from rest_framework import serializers, viewsets
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class FilterItemViewSet(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_fields = ["id", "category", "label"]
    ordering_filter = ["id", "price", "title"]
    search_fields = ["title", "description"]






