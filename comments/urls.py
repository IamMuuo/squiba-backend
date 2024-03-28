"""Posts url file.

Contains all the urls related to posts
"""

from django.urls import path
from .views import CreateComment, ListComments, DeleteComment

urlpatterns = [
    path(
        "create/",
        CreateComment.as_view(),
        name="comment-create",
    ),
    path(
        "find/<int:post>",
        ListComments.as_view(),
        name="list-comments",
    ),
    path(
        "delete/<int:id>",
        DeleteComment.as_view(),
        name="delete-comments",
    ),
]
