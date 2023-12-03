from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    "decemeber":"Go to walk!"
}


def all_challenges(request):
    all_months = list(monthly_challenges.keys())
    months_links = []
    for month in all_months:
        redirect_link = f"""
        <ul>
            <li><h2><a style="text-decoration: none;" href=\"{reverse("month-challenge", args=[month])}\"> {month.capitalize()}</a></h2></li>
        </ul>
        """
        months_links.append(redirect_link)
    
    return HttpResponse(content=months_links)



def monthly_challenges_by_number(request, month:int):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>× Invalid month!</h1>")
    redirect_month = months[month-1]

    return HttpResponseRedirect(reverse("month-challenge",args=[redirect_month]))


def monthly_challenge(request, month:str):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not found!")