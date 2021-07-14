from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets, mixins
from rest_framework import permissions
from adminapp.models import Subscription, Exhibit, Faq

from .serialiers import UserSerializer, SubscriptionSerializer, ExhibitSerializer, FaqSerializer

User = get_user_model()


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    # Allow authenticated user to access this url
    permission_classes = [permissions.IsAdminUser]


class ExhibitView(generics.ListAPIView):
    serializer_class = ExhibitSerializer
    queryset = Exhibit.objects.all()


class ExhibitDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'uuid'
    serializer_class = ExhibitSerializer
    queryset = Exhibit.objects.all()


class SubscriptionViewSet(viewsets.GenericViewSet,
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin
                          ):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class FaqView(generics.ListAPIView):
    serializer_class = FaqSerializer
    queryset = Faq.objects.all()
    permission_class = [permissions.IsAdminUser]
