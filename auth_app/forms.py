from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from auth_app.models import CustomUserModel

# Custom UserCreationForm and UserChangeForm


# For adding a new user through admin site
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ["email", "phone_number"]


# For updating or changing a user through admin site.
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUserModel
        fields = "__all__"


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
