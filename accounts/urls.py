from django.urls import path
from .views import (
    CustomUserCreateView,
    CustomUserListView,
    CustomUserRetrieveUpdateDestroyView,
    LoginView,
)

urlpatterns = [
    path(
        "register/",
        CustomUserCreateView.as_view(),
        name="user-list-create",
    ),
    path(
        "all/",
        CustomUserListView.as_view(),
        name="user-list",
    ),
    path(
        "info/<int:pk>/",
        CustomUserRetrieveUpdateDestroyView.as_view(),
        name="user-detail",
    ),
    path(
        "auth/",
        LoginView.as_view(),
        name="authentication",
    ),
]
