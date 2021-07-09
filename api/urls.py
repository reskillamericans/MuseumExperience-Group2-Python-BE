import api
from django.urls import path, include 
import api.views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('subscription', api.views.SubscriptionViewSet, basename='subscription')


urlpatterns = [
    path('', include(router.urls)),
]