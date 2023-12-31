from django.urls import path

from challenges.views import monthly_challenge, monthly_challenges_by_number, index

urlpatterns = [
    path("", index, name="index"),
    path("<int:month>", monthly_challenges_by_number, name="month-challenge-by-number"),
    path("<str:month>", monthly_challenge, name="month-challenge"),
]