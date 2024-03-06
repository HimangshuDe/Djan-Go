from django.views.generic import ListView, DetailView

from .models import Post


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


class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = Post.objects.get(slug=self.kwargs["slug"]).tags.all()
        return context


# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(
#         request,
#         "blog/post-detail.html",
#         {"post": identified_post, "post_tags": identified_post.tags.all()},
#     )
