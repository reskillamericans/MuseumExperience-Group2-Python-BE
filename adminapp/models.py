import uuid
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'visitor'),
        (2, 'staff'),
        (3, 'curator'),
        (4, 'admin'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=None, null=True, blank=True)
    username = models.CharField(max_length=100, unique=True, blank=True, null=True, default=None)
    email = models.EmailField(max_length=500, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "user"  # replace plural with singular verb

    def __str__(self):
        return self.email


class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='user_profile_id')
    phone_number = models.CharField(max_length=512, null=True, default=None, blank=True)
    age = models.IntegerField(null=True, blank=True, default=None)
    birthday = models.CharField(null=True, max_length=255, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class Exhibit(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=512, null=True, blank=True, default=None)
    description = models.TextField(default=None, null=True, blank=True)
    images = models.JSONField(default=None, null=True, blank=True)
    video = models.URLField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "exhibit_status"  # replace plural with singular verb

    def __str__(self):
        return self.name


class Exhibit_Notification(models.Model):
    exhibit_id = models.ForeignKey(Exhibit, on_delete=models.DO_NOTHING, related_name='exhibits_id')
    notification = models.CharField(max_length=512, blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.exhibit_id.uuid


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_question_id')
    question = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='subscriber_id')
    exhibits = models.ManyToManyField(Exhibit)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)
 