from django.shortcuts import get_object_or_404, render
from datetime import date
from .models import Post


def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/starting-page.html", {"posts": latest_posts})

def all_posts(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": posts
    })

def post_detail(request, slug):
    identified_post = get_object_or_404(Post,slug=slug)
    return render(request, "blog/post-detail.html", {
        "post":identified_post,
        "post_tags":identified_post.tags.all()
    })