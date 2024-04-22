"""Post Serializer."""

from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """The post serializer to be used."""

    content = serializers.SerializerMethodField("get_image_url")

    def get_image_url(self, obj):
        """Return the image with its full url."""
        request = self.context.get("request")
        return request.build_absolute_uri(obj.content.url)

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
