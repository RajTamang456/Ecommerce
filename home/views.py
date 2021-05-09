from django.shortcuts import render
from django.views.generic import View
from .models import *
# Create your views here.
class BaseView(View):
    views = {}

class HomeView(BaseView):
    def get(self,request):
        self.views['category'] = Category.objects.filter(status = 'active')
        self.views['sliders'] = Slider.objects.filter(status = 'active')
        self.views['ad'] = Ad.objects.all()
        self.views['brand'] = Brand.objects.filter(status = 'active')
        self.views['hot'] = Item.objects.filter(status = 'active', label = 'hot')
        self.views['new'] = Item.objects.filter(status = 'active', label = 'new')

        return render(request, 'index.html', self.views)