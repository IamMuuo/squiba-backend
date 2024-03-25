"""Posts url file.

Contains all the urls related to posts
"""

from django.urls import path
from .views import (
    PostList,
    UserPostListing,
    LikePostView,
    DeletePostView,
    PostListings,
)

urlpatterns = [
    path(
        "create/",
        PostList.as_view(),
        name="post-create",
    ),
    path(
        "listings/",
        PostListings.as_view(),
        name="post-listing",
    ),
    path(
        "find/<int:user_id>",
        UserPostListing.as_view(),
        name="find-post-listing",
    ),
    path(
        "like/<int:id>",
        LikePostView.as_view(),
        name="like-post",
    ),
    path(
        "delete/<int:pk>",
        DeletePostView.as_view(),
        name="delete-post",
    ),
]
