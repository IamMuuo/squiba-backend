# Generated by Django 5.0.2 on 2024-02-27 12:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("stories", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="StoryPost",
            new_name="Story",
        ),
    ]
