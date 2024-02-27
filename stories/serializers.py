from rest_framework import serializers
from .models import Story


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ["user", "text", "content", "date_uploaded", "date_of_expiry"]
