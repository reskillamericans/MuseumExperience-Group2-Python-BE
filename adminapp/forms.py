from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import User, Visitor, Staff, Curator, Admin  

class VisitorSignUpForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    
    class Meta(UserCreationForm.Meta):
        model = User 

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = 1
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.save()
        visitor = Visitor.objects.create(user=user)
        visitor.save()
        return user


class StaffSignUpForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    User_Type_Choices =(
        (2,'staff'),
        (3, 'curator'),
        (4,'admin'),
        )
    staff_type = forms.MultipleChoiceField(choices=User_Type_Choices)
    
    class Meta(UserCreationForm.Meta):
        model = User 

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.user_type = int(self.cleaned_data.get('staff_type')[0]) 
        user.save()
        if user.user_type == 2:
            staff = Staff.objects.create(user=user)
        elif user.user_type == 3:
            staff = Curator.objects.create(user=user)
        elif user.user_type == 4:
            staff = Admin.objects.create(user=user)
        staff.save()
        return user
