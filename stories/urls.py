from django.urls import path
from .views import StoryList, StoryDetail

urlpatterns = [
    path("create/", StoryList.as_view(), name="story-list"),
    path("find/<int:pk>/", StoryDetail.as_view(), name="story-detail"),
]
