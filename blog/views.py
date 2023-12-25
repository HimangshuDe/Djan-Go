from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request, "blog/starting-page.html")

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail-page.html")