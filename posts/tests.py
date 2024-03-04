"""Tests.

Tests for the posts service
"""

from django.test import TestCase, Client
from accounts.models import CustomUser as User
from django.urls import reverse
from .models import Post


# Create your tests here.
class PostViewTest(TestCase):
    """PostViewTest.

    Tests the post view
    """

    def setUp(self):
        """Instanciate an instance."""
        self.client = Client()
        self.user = User.objects.create_user(
            first_name="test",
            last_name="test",
            mobile_phone_number="070707070",
            # username="testuser",
            password="12345",
            email="testuser@example.com",
        )
        self.post = Post.objects.create(
            user=self.user,
            description="Test Post",
            likes=0,
        )

    def test_post_list_view(self):
        """Test that a post was created."""
        response = self.client.get(reverse("post-listing"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    def test_user_post_listing_view(self):
        """Test a users's posts can be retieved."""
        response = self.client.get(
            reverse("find-post-listing", kwargs={"user_id": self.user.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    # def test_like_post_view(self):
    #     """Test a user can like a post."""
    #     # self.client.login(username="testuser", password="12345")
    #     response = self.client.patch(
    #         reverse(
    #             "like-post",
    #             kwargs={
    #                 "user_id": self.user.id,
    #                 "id": self.post.id,
    #             },
    #         )
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Test Post")
