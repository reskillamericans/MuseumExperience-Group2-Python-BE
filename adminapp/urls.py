from django.urls import path, include 
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('subscription', views.SubscriptionViewSet, basename='subscription')

urlpatterns = [
    path('', views.index, name="index"),
    # path('users', views.UserView.as_view(), name="user"),
    path('register', views.register, name='register'),
    path('register/visitor', views.visitor_register.as_view(), name='visitor_register'),
    path('register/staff', views.staff_register.as_view(), name='staff_register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('user', views.UserView.as_view(), name="user"),
    path('', include(router.urls))
]  