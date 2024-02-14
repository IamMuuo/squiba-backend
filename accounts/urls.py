from django.urls import path
from .views import CustomUserListCreateView, CustomUserRetrieveUpdateDestroyView

urlpatterns = [
    path(
        "register/",
        CustomUserListCreateView.as_view(),
        name="user-list-create",
    ),
    path(
        "info/<int:pk>/",
        CustomUserRetrieveUpdateDestroyView.as_view(),
        name="user-detail",
    ),
]