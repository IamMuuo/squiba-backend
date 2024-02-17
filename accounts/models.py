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
        first_name = extra_fields.get("first_name")
        last_name = extra_fields.get("last_name")
        mobile_phone_number = extra_fields.get("mobile_phone_number")
        if not first_name:
            raise ValueError("First name cannot be empty")
        if not last_name:
            raise ValueError("Last name cannot be empty")
        if not mobile_phone_number:
            raise ValueError("Mobile phone number is required")

        if not email:
            raise ValueError("Email cannot be empty")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    Custom user model to be used in the application
    """

    email = models.EmailField(unique=True, null=False, blank=False)
    mobile_phone_number = models.CharField(max_length=15, null=False, blank=False)
    profile_photo = models.ImageField(upload_to="", null=True, blank=True)
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
