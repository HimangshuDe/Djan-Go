from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View
from django.shortcuts import render

from blog.forms import CommentForm

from .models import Comment, Post


def get_date(post):
    return post["date"]


# Create your views here.


class StartingPageView(ListView):
    template_name = "blog/starting-page.html"
    model = Post
    queryset = Post.objects.all().order_by("-date")[:3]
    context_object_name = "posts"

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     data = queryset[:3]
    #     return data


# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/starting-page.html", {"posts": latest_posts})


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


# def all_posts(request):
#     posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {"all_posts": posts})


class SinglePostView(View):

    def is_stored_post(self, request, post_id):
        stored_post = request.session.get("stored_posts")
        if stored_post is None:
            is_saved_for_later = False
        else:
            is_saved_for_later = post_id in stored_post
        return is_saved_for_later

    # GET request
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "all_comment": post.comments.all().order_by("-id"),
            "comment_form": CommentForm(),
            "is_saved_for_later": self.is_stored_post(request, post.id),
        }
        return render(request, "blog/post-detail.html", context)

    # POST request
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "all_comment": post.comments.all().order_by("-id"),
            "comment_form": comment_form,
            "is_saved_for_later": self.is_stored_post(request, post.id),
        }
        return render(request, "blog/post-detail.html", context)


# def post_detail(request, slug):
# identified_post = get_object_or_404(Post, slug=slug)
# return render(
#     request,
#     "blog/post-detail.html",
#     {"post": identified_post, "post_tags": identified_post.tags.all()},
# )


class ReadLaterView(View):
    # GET request
    def get(self, request):
        stored_post = request.session.get("stored_posts")
        context = {}
        if stored_post is None or len(stored_post) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_post)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/read-later.html", context)

    #  POST request
    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)

        else:
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect(reverse("starting-page"))
