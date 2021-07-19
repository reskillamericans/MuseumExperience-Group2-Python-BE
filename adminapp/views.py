from django.db.models import fields
from adminapp.models import Exhibit
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import CreateView
from .forms import VisitorSignUpForm, StaffSignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.decorators import api_view, permission_classes #added my Morris - may or may not be needed for authentication 
from rest_framework.permissions import IsAuthenticated #added my Morris - may or may not be needed for authentication 
User = get_user_model()

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

class visitor_register(CreateView):
    model = User
    form_class = VisitorSignUpForm
    template_name = 'visitor_register.html'
    success_url = '/'

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid

class staff_register(CreateView):
    model = User
    form_class = StaffSignUpForm
    template_name = 'staff_register.html'
    success_url = '/'

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    return render(request, 'login.html', context={'login_form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')








