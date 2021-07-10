from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets, mixins

from adminapp.models import Subscription, Exhibit

from .serialiers import UserSerializer, SubscriptionSerializer, ExhibitSerializer

User = get_user_model()


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


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
