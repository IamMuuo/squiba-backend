from rest_framework import generics
from rest_framework.views import APIView, Response, status
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.contrib.auth import authenticate, login, logout


class CustomUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class LoginView(APIView):
    """Authentication API."""

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response(
            {"message": "Successfully logged out"}, status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            serializer = CustomUserSerializer(user)
            # print(serializer.data)
            # serializer.data["profile_photo"] = (
            #     request.META["SERVER_NAME"] + serializer.data["profile_photo"]
            # )
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
