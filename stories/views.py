from datetime import datetime, timezone
from rest_framework import generics
from .models import Story
from .serializers import StorySerializer

# Create your views here.


class StoryList(generics.ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    def get_queryset(self):
        # Filter stories to only include those that have not yet expired
        return Story.objects.filter(date_of_expiry__gt=datetime.now())


# Retrieve, update or delete a story instance
class StoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
