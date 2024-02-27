from datetime import datetime, time
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.

CustomUser = get_user_model()


class Story(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    content = models.ImageField(upload_to="story_posts/", null=True, blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_of_expiry = models.DateTimeField()

    def __str__(self):
        return self.text[
            :50
        ]  # Return the first   50 characters of the text for display

    def save(self, *args, **kwargs):
        # If the instance is being created, set the date_of_expiry to  24 hours after date_uploaded
        if not self.pk:
            self.date_of_expiry = datetime.now() + timezone.timedelta(hours=24)
        super().save(*args, **kwargs)
