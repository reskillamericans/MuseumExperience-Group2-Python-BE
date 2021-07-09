# import serializers from rest_framework
from rest_framework import serializers
from django.contrib.auth.models import User

# import models from models.py
from .models import User, User_Profile, Exhibit, Exhibit_Notification, Question, Subscription


# create a model serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # specify field names
        fields = ['user_type', 'username', 'email']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Profile
        # specify field names
        fields = ['id', 'phone_number', 'age', 'birthday', 'created_at', 'updated_at']


class ExhibitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibit
        fields = ['uuid', 'name', 'description', 'images', 'video']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibit_Notification
        fields = ['exhibit_id', 'notification', 'created_at', 'updated_at']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['uuid', 'user', 'exhibits'] 

