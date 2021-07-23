# import serializers from rest_framework
from rest_framework import serializers
from django.contrib.auth import get_user_model
# import models from models.py
from adminapp.models import (User, User_Profile, Exhibit,
                            Exhibit_Notification, Question, Subscription, Faq)
from rest_framework.validators import UniqueValidator                          


User = get_user_model()

# create a model serializer
class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model = User
        fields = ['id', 'user_type', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


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
    question = serializers.CharField(required=True)
    class Meta:
        model = Question
        fields = ['id', 'question', 'user', 'created_at', 'answered']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['uuid', 'user', 'exhibits']


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ['id', 'question', 'answer']


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password', ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        #validate_password(value)
        return value

    def create(self, validated_data):
        user = get_user_model()(**validated_data)

        user.set_password(validated_data['password'])
        user.save()

        return user
