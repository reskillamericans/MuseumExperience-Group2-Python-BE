import api.views
from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('subscription', api.views.SubscriptionViewSet, basename='subscription')

urlpatterns = [
    path('', include(router.urls)),
    path('get-exhibits', api.views.ExhibitView.as_view(), name='get-exhibits'),
    url(r'^get-exhibits-details/(?P<uuid>.*)$', api.views.ExhibitDetail.as_view()),
    url(r'^create-user/$', api.views.CreateUserView.as_view()),
    path('faqs', api.views.FaqView.as_view(), name='faq')
]
