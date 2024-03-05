from django.urls import path

from . import views

urlpatterns = [
    path("profiles/", views.CreateProfileView.as_view(), name="create_profile"),
    path("profiles/list", views.ProfilesView.as_view(), name="all_profiles"),
]
