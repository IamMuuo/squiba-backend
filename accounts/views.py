"""Account views.

Api methods.
"""

from rest_framework import generics
from rest_framework.views import APIView, Response, status
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.contrib.auth import authenticate, login, logout


class CustomUserCreateView(generics.CreateAPIView):
    """Create a user."""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserListView(generics.ListAPIView):
    """List all users."""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve and update a user info."""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class LoginView(APIView):
    """Authentication API."""

    def get(self, request, *args, **kwargs):
        """Logout a user."""
        logout(request)
        return Response(
            {"message": "Successfully logged out"}, status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        """Login a user."""
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            serializer = CustomUserSerializer(user)
            print(request.get_host())
            data = serializer.data
            if data["profile_photo"] is not None:
                data["profile_photo"] = (
                    "http://" + request.get_host() + data["profile_photo"]
                )

            return Response(data, status=status.HTTP_200_OK)

        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
            )


class FeaturedApiView(generics.ListAPIView):
    """An api to return featured users."""

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all().order_by("?")[:10]


# class SearchApiView(generics.RetrieveAPIView):
#     """Search for a user by username."""
#
#     serializer_class = CustomUserSerializer
#     queryset = CustomUser.objects.all()
#


class SearchApiView(generics.RetrieveAPIView):
    """Search for a user by first name, last name, or username."""

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class DeleteUserApiView(generics.DestroyAPIView):
    """
    DeleteUserApiView.

    Delete a user from the database.
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
