from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets, mixins

from adminapp.models import Subscription

from .serialiers import UserSerializer, SubscriptionSerializer

User = get_user_model()


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class SubscriptionViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin
                     ):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer