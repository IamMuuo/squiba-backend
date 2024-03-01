"""Post views.

Contains all views related to the Post service
"""

from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


# Create your views here.
class PostList(generics.ListCreateAPIView):
    """PostList.

    Handles functionality for post creation
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserPostListing(generics.ListAPIView):
    """UserPostListing.

    Retrieves all posts pertaining a certain user
    """

    serializer_class = PostSerializer

    def get_queryset(self):
        """Return a actual user posts."""
        user_id = self.kwargs["user_id"]
        return Post.objects.filter(user_id=user_id)
