from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token
from adminapp.models import (User, User_Profile, Exhibit,
                            Exhibit_Notification, Question, Subscription, Faq)
from rest_framework.validators import UniqueValidator                          


User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Profile
        fields = ['phone_number', 'age', 'birthday']

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(required=True)
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    user_profile_id = ProfileSerializer()
    password = serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model = User
        fields = ('full_name', 'username', 'email', 'user_profile_id', 'password')

    def create(self, validated_data):
        username = validated_data.get('username')
        full_name = validated_data.get('full_name')
        email = validated_data.get('email')
        password = validated_data.get('password')

        user = User.objects.create_user(username=username, full_name=full_name, email=email, password=password)

        profile_data = validated_data.pop('user_profile_id')
        phone_number = profile_data.get('address')
        age = profile_data.get('age')
        birthday = profile_data.get('birthday')
        profile = User_Profile(user=user, phone_number=phone_number, age=age, birthday=birthday)
        profile.save()
        return user


class CustomUserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)
    token = serializers.CharField(read_only=True, allow_blank=False)

    class Meta:
        model = User
        fields = ['email', 'password', 'token']

    
    def validate(self, data):
        email = data.get('email', None)
        passw = data.get('password', None)
        
        #check if email field is empty
        if not email and not passw:
            raise serializers.ValidationError("Please enter your email address")

        #check if email is valid
        user = authenticate(email=email, password=passw)

        if not user:
            raise serializers.ValidationError("Invalid Credentials")

        #check if user is active and get or create user token
        if user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            data['token'] = token
        else:
            raise serializers.ValidationError("User not active")

        return data



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
