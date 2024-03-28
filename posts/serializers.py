"""Post Serializer."""

from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """The post serializer to be used."""

    class Meta:
        """Define the fields to be used by a serializer."""

        model = Post
        fields = [
            "id",
            "user",
            "content",
            "date_posted",
            "description",
            "likes",
            "liked_by",
        ]
