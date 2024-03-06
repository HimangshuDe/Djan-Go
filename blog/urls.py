from django.urls import path
from blog.views import StartingPageView, AllPostsView, SinglePostView

urlpatterns = [
    path("", StartingPageView.as_view(), name="starting-page"),
    path("posts/", AllPostsView.as_view(), name="posts-page"),
    path(
        "posts/<slug:slug>", SinglePostView.as_view(), name="post-detail-page"
    ),  # posts/my-first-postpost_details
]
