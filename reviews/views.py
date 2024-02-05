from django.http import HttpResponseRedirect
from django.shortcuts import render

from reviews.forms import ReviewForm

# Create your views here.

def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # print(form.cleaned_data["user_name"])
            # entered_username = form.cleaned_data["user_name"]
            return HttpResponseRedirect("/thank-you")

    form = ReviewForm()

    return render(request, "reviews/review.html", {"has_error":False, "form":form})


def thank_you(request):
    return render(request, "reviews/thank_you.html")