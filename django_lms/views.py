from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from courses.models import Course
from django.shortcuts import render

class UserProfile(LoginRequiredMixin, generic.ListView):
    model = Course
    template_name = 'user_profile.html'

def index(request):
    return render(request, 'index.html')

def courcedetails(request):
    return render(request, 'cource-details.html')

def cource(request):
    return render(request, 'courses.html')

def custom(request):
    return render(request, 'custom.html')

def events(request):
    return render(request, 'events.html')

def pricing(request):
    return render(request, 'pricing.html')

def trainers(request):
    return render(request, 'trainers.html')

def homes(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')