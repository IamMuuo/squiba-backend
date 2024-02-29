from django.urls import path
from .views import PostList

urlpatterns = [
    path("listings/", PostList.as_view(), name="story-list"),
]
