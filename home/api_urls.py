from django.urls import path, include
from django.contrib.auth.models import User


# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers

from home.views import FilterItemViewSet, ItemViewSet

router = routers.DefaultRouter()
router.register(r'users', ItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('items/', FilterItemViewSet.as_view(), name='items')
]