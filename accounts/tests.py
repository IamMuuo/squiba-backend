from django.test import TestCase
from accounts.models import CustomUser
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your tests here.
class CustomUserModelTest(TestCase):
    def test_create_user(self):
        # Test creating a user with email and mobile phone number
        user = CustomUser.objects.create_user(
            email="testuser@example.com",
            mobile_phone_number="1234567890",
            password="testpassword123",
            first_name="Test",
            last_name="User",
        )
        self.assertEqual(user.email, "testuser@example.com")
        self.assertEqual(user.mobile_phone_number, "1234567890")
        self.assertTrue(user.check_password("testpassword123"))
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")

    def test_create_user_with_profile_photo(self):
        # Test creating a user with a profile photo
        photo_content = b"file_content"
        photo = SimpleUploadedFile(
            "test_photo.jpg", photo_content, content_type="image/jpeg"
        )
        user = CustomUser.objects.create_user(
            email="testuser@example.com",
            mobile_phone_number="1234567890",
            password="testpassword123",
            first_name="Test",
            last_name="User",
            profile_photo=photo,
        )
        saved_photo = user.profile_photo.open()
        saved_photo_content = saved_photo.read()
        saved_photo.close()

        # Assert that the contents of the uploaded file are equal to the contents of the saved file
        self.assertEqual(photo_content, saved_photo_content)

    def test_create_user_with_empty_first_name_and_last_name(self):
        # Test creating a user with empty first name and last name
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(
                email="testuser@example.com",
                mobile_phone_number="1234567890",
                password="testpassword123",
                first_name="",
                last_name="",
            )

    def test_create_user_with_empty_email(self):
        # Test creating a user with empty email
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(
                email="",
                mobile_phone_number="1234567890",
                password="testpassword123",
                first_name="Test",
                last_name="User",
            )

    def test_create_user_with_empty_mobile_phone_number(self):
        # Test creating a user with empty mobile phone number
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(
                email="testuser@example.com",
                mobile_phone_number="",
                password="testpassword123",
                first_name="Test",
                last_name="User",
            )
