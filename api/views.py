from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets, mixins, filters
from rest_framework import permissions
from adminapp.models import Subscription, Exhibit, Faq, Question
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .serialiers import UserSerializer, SubscriptionSerializer, ExhibitSerializer, FaqSerializer, QuestionSerializer

User = get_user_model()


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

class CreateUserView(generics.CreateAPIView):
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


class FaqView(generics.ListAPIView):
    serializer_class = FaqSerializer
    queryset = Faq.objects.all()
    permission_class = [permissions.IsAdminUser, permissions.IsAuthenticated]


class QuestionsAPIView(ListCreateAPIView):
    filterset_fields = {
            'question': ['contains'],
            'user__email': ['exact'],
            'created_at': ['exact'],
            'answered': ['exact']
        }
    ordering = ['created_at']
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter,] 
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer