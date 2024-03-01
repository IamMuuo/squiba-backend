"""Posts url file.

Contains all the urls related to posts
"""

from django.urls import path
from .views import PostList, UserPostListing

urlpatterns = [
    path("listings/", PostList.as_view(), name="post-listing"),
    path(
        "find/<int:user_id>",
        UserPostListing.as_view(),
        name="find-post-listing",
    ),
]
