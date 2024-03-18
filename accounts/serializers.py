from rest_framework import serializers

from accounts.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """Serialize the user model."""

    class Meta:
        """Meta class defining fields to be serialized."""

        model = CustomUser
        fields = (
            "username",
            "id",
            "first_name",
            "last_name",
            "email",
            "mobile_phone_number",
            "profile_photo",
            "password",
            "is_staff",
            "is_active",
            "date_joined",
            "last_login",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """Save instace."""
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        """Update instance."""
        # Check if the password field is included in the validated data
        password = validated_data.pop("password", None)
        if password:
            # Hash the password and set it on the instance
            instance.set_password(password)
        # Update the other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
