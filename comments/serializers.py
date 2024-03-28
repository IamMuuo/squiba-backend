"""Comment Serializer.

Contains functionality for serializing and deserializing
data to and from json into a usable model.
"""

from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """The actual serializer class."""

    class Meta:
        """Defines the model fields to be used."""

        model = Comment
        fields = [
            "id",
            "user",
            "content",
            "created_at",
            "updated_at",
        ]
