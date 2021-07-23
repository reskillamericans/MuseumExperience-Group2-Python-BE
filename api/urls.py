import api.views
from django.urls import path, include, re_path
from django.conf.urls import url
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView
from dj_rest_auth.views import LoginView, LogoutView
from allauth.account.views import ConfirmEmailView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('subscription', api.views.SubscriptionViewSet, basename='subscription')

urlpatterns = [
     path('', include(router.urls)),
     path('get-exhibits', api.views.ExhibitView.as_view(), name='get-exhibits'),
     url(r'^get-exhibits-details/(?P<uuid>.*)$', api.views.ExhibitDetail.as_view()),
     url(r'^create-user/$', api.views.UserView.as_view()),
     path('faqs', api.views.FaqView.as_view(), name='faq'),
     path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),

     path('register/', RegisterView.as_view()),
     path('login/', api.views.UserLogin.as_view()),
     path('logout/', LogoutView.as_view()),
     path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
     path('account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
     re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),
     path('question', api.views.QuestionView.as_view()),
     path('exhibit', api.views.ExhibitView.as_view()),
     path('search', api.views.SearchView.as_view()),
     # path('create-user', api.views.CreateUserView.as_view()),
]
