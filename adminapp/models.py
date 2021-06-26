from django.db import models
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Exhibit(models.Model):
    exhibit_name = models.CharField(max_length=500)
    exhibit_start = models.DateField(default=datetime.today)
    exhbit_end = models.DateField(default=datetime.today)

    class Exhibit_Status(models.TextChoices):
        temporary = 'Temporary'
        feature = 'Feature'

    exhibit_status = models.CharField(max_length=20,choices = Exhibit_Status.choices, default = Exhibit_Status.temporary)

    class Meta:
        verbose_name_plural = "exhibit" # replace plural with singular verb 

    def __str__(self):
        return self.exhibit_name


class Exhibit_Notification(models.Model):
    exhibit_id = models.IntegerField()
    notification = models.CharField(max_length=500)

class Question(models.Model):
    question = models.CharField(max_length=300)
    # answer = Field.blank()

    def __str__(self):
        return self.question


class User(AbstractUser):
    User_Type_Choices =(
        (1, 'visitor'),
        (2,'staff'),
        (3, 'curator'),
        (4,'admin'),
        )
    user_type = models.PositiveSmallIntegerField(choices=User_Type_Choices)

    username = models.CharField(max_length=100, unique = True)
    email = models.EmailField(max_length=500, unique= True)
    class Meta:
        verbose_name_plural = "user" # replace plural with singular verb 

    def __str__(self):
        return self.email

class User_Porfile(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    age = models.IntegerField()
    birthday = models.DateField(default=datetime.today)
    residence_zipcode = models.IntegerField()

    def __str__(self):
        return self.user



#upload this link
