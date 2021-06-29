from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import CreateView
from .models import User, Visitor, Staff, Curator, Admin
from .forms import VisitorSignUpForm, StaffSignUpForm
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return HttpResponse("<h1>Museum Admin App</h1>")

def register(request):
    return render(request, 'register.html')

class visitor_register(CreateView):
    model = User
    form_class = VisitorSignUpForm
    template_name = 'visitor_register.html'

    def validation(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class staff_register(CreateView):
    model = User
    form_class = StaffSignUpForm
    template_name = 'staff_register.html'

    def validation(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')