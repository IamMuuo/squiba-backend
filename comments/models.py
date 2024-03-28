"""Comment Model.

Defines the structure of a comment.
"""

from django.db import models
from stories.models import CustomUser
from posts.models import Post


# Create your models here.
class Comment(models.Model):
    """Comment.

    The comment model describes the structure of a comment.
    """

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Define the ordering of data."""

        ordering = ("created_at",)

    def __str__(self):
        """Return a string representation of the comment."""
        return self.content[:50]
