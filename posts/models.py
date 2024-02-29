from django.db import models

# from .comments import Comment

from stories.models import CustomUser


class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    likes = models.IntegerField()
    liked_by = models.ManyToManyField(
        CustomUser, related_name="liked_posts", blank=True
    )

    content = models.ImageField(upload_to="posts/", null=True, blank=True)
    # Assuming you have a Comment model with a ForeignKey to Post
    # comments = models.ManyToManyField(Comment, related_name="post_comments", blank=True)

    def __str__(self):
        return self.description[:50]
