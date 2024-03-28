"""Comment Views.

Defines the functionality for CRUD of comments
"""

from rest_framework import generics

# from posts.models import Post
from .models import Comment
from .serializers import CommentSerializer


class CreateComment(generics.CreateAPIView):
    """Create Comment.

    Creates a comment
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ListComments(generics.ListAPIView):
    """List Comments.

    Lists a comment related to a post
    """

    def get_queryset(self):
        """Return a actual user posts."""
        post = self.kwargs["post"]
        return Comment.objects.filter(post=post)

    serializer_class = CommentSerializer
    lookup_field = "post"


class DeleteComment(generics.DestroyAPIView):
    """Delete Comment.

    Deletes a comment from the database.
    """

    def get_queryset(self):
        """Get the query parameters."""
        id = self.kwargs["id"]
        return Comment.objects.filter(id=id)

    serializer_class = CommentSerializer
    lookup_field = "id"
