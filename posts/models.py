"""Post Models.

Defines post models to be used by the post service
"""

from django.db import models
from stories.models import CustomUser


class Post(models.Model):
    """Post.

    Represent a post
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    likes = models.IntegerField()
    liked_by = models.ManyToManyField(
        CustomUser,
        related_name="liked_posts",
        blank=True,
    )

    content = models.ImageField(
        upload_to="posts/",
        null=True,
        blank=True,
    )

    def __str__(self):
        """Return a string representation of a post."""
        return self.description[:50]
