from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import TemplateView

# Create your views here.


class HomeView(TemplateView):
    template_name = "auth_app/home.html"


def profile_detail_view(request):
    return render(request, "auth_app/profile_detail.html")


# Creating login view for login
def login_view(request):
    return render(request, "auth_app/login.html")


# For registering new users
def register_view(request):
    return render(request, "auth_app/register.html")


# For logging out users
def logout_view(request):
    return HttpResponsePermanentRedirect(reverse("home"))
