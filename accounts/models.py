from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


# Custom user manager
class CustomUserManager(BaseUserManager):
    """
    Manages user info
    """

    def create_user(self, email, password, **extra_fields):
        """
        Validates the user field before saving
        """
        if not email:
            raise ValueError("Email cannot be empty")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user


class CustomUser(AbstractUser):
    """
    Custom user model to be used in the application
    """

    email = models.EmailField(unique=True, null=False, blank=False)
    mobile_phone_number = models.CharField(max_length=15, null=False, blank=False)
    profile_photo = models.ImageField(
        upload_to="profile_photos/", null=True, blank=True
    )
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)

    username = None

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "mobile_phone_number",
    ]

    def __str__(self) -> str:
        return str(self.email)
