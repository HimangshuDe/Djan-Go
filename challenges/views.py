from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january":"Be veg this month!",
    "february":"Go to walk!",
    "march":"Learn Python!",
    "april":"Go to Gym!",
    "june":"Be spiritual!",
    "july":"Learn Python!",
    "august":"Go to walk!",
    "september":"Go to Gym!",
    "october":"Be veg this month!",
    "november":"Learn Python!",
    # "decemeber":"Go to walk!"
    "decemeber":None
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months":months
    })



def monthly_challenges_by_number(request, month:int):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>× Invalid month!</h1>")
    redirect_month = months[month-1]

    return HttpResponseRedirect(reverse("month-challenge",args=[redirect_month]))


def monthly_challenge(request, month:str):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name":month,
            "challenge_text":challenge_text
        }) 
        #NOTE: The above line does the exact thing, what the below two lines does!
    
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)

    except:
        raise Http404()