"""Posts url file.

Contains all the urls related to posts
"""

from django.urls import path
from .views import CreateComment

urlpatterns = [
    path(
        "create/",
        CreateComment.as_view(),
        name="comment-create",
    ),
]
