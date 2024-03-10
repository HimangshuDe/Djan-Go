from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout

from auth_app.forms import CustomUserCreationForm, LoginForm

# Create your views here.


class HomeView(TemplateView):
    template_name = "auth_app/home.html"


def profile_detail_view(request):
    if not request.user.is_authenticated:  # usual way of authenticating a user
        return HttpResponseRedirect(reverse("login") + "?next=/profile/")

    # if user is authenticated
    context = {
        "user": request.user,
    }
    return render(request, "auth_app/profile_detail.html", context)


# Creating login view for login
def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # we use authenticate to log in a user by authenticate() function
            # which takes credentials as input and returns a user object if valid else none
            user = authenticate(
                email=form.cleaned_data["email"], password=form.cleaned_data["password"]
            )
            if user is not None:
                login(request, user)
                if request.GET.get("next"):
                    return HttpResponseRedirect(request.GET.get("next"))
                return HttpResponseRedirect(reverse("home"))
            else:
                return render(
                    request,
                    "auth_app/login_page.html",
                    {"form": form, "error_messages": "Invalid Credentials"},
                )
        return render(request, "auth_app/login_page.html", {"form": form})

    return render(request, "auth_app/login_page.html", {"form": form})


# For registering new users
def register_view(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user_email = form.cleaned_data["email"]
            user_password = form.cleaned_data["password2"]
            user = authenticate(email=user_email, password=user_password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("home"))

        return render(request, "auth_app/register.html", {"form": form})

    return render(request, "auth_app/register.html", {"form": form})


# For logging out users
def logout_view(request):
    logout(request)
    return HttpResponsePermanentRedirect(reverse("home"))
