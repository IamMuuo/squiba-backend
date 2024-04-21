"""Post views.

Contains all views related to the Post service
"""

from accounts.models import CustomUser
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from .models import Post
from .serializers import PostSerializer


# Create your views here.
class PostList(generics.CreateAPIView):
    """PostList.

    Handles functionality for post creation
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostListings(generics.ListAPIView):
    """PostListings."""

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


class LikePostView(generics.UpdateAPIView):
    """LikePostView.

    Logic for the liking functionality
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def patch(self, request, *args, **kwargs):
        """patch.

        This method adds or reduces the number of likes depending on the user
        submitting the like
        """
        post = None
        user = None
        try:
            post_id = self.kwargs["id"]
            post = Post.objects.get(id=post_id)
            user_id = request.data["user_id"]
            user = CustomUser.objects.get(id=user_id)
        except Post.DoesNotExist:
            return Response(
                data={"error": "Post not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except CustomUser.DoesNotExist:
            return Response(
                data={
                    "error": "user does not exit",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        if post is None:
            return Response(
                data={"error": "Post not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        if user in post.liked_by.all():
            print("if")
            post.liked_by.remove(user)
            post.likes -= 1
        else:
            print("else")
            post.liked_by.add(user)
            post.likes += 1

        post.save()
        serializer = self.get_serializer(post)
        return Response(serializer.data)


class DeletePostView(generics.DestroyAPIView):
    """DeletePostView.

    This method deletes a post from the server
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class FeaturedPostView(generics.ListAPIView):
    """An api to return featured posts."""

    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by("?")[:20]
