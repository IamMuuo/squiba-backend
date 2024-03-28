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
