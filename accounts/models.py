from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


# Custom user manager
class CustomUserManager(BaseUserManager):
    """Manage user info."""

    def create_user(self, username, email, password, **extra_fields):
        """Validate the user field before saving."""
        first_name = extra_fields.get("first_name")
        last_name = extra_fields.get("last_name")
        mobile_phone_number = extra_fields.get("mobile_phone_number")
        if not first_name:
            raise ValueError("First name cannot be empty")
        if not last_name:
            raise ValueError("Last name cannot be empty")
        if not mobile_phone_number:
            raise ValueError("Mobile phone number is required")
        if not username:
            raise ValueError("Username cannot be empty")
        if not email:
            raise ValueError("Email cannot be empty")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """Set the defaults on the superuser."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    """Custom user model to be used in the application."""

    email = models.EmailField(unique=True, null=False, blank=False)
    mobile_phone_number = models.CharField(
        unique=True,
        max_length=15,
        null=False,
        blank=False,
    )
    profile_photo = models.ImageField(upload_to="", null=True, blank=True)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    username = models.CharField(
        max_length=60,
        null=False,
        unique=True,
        blank=False,
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "email",
        "first_name",
        "last_name",
        "mobile_phone_number",
    ]

    def __str__(self) -> str:
        """Return a string representation of the user."""
        return str(self.email)
