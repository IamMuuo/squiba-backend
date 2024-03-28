# Generated by Django 5.0.2 on 2024-03-28 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0004_alter_comment_id"),
        ("posts", "0010_remove_post_comments_post_comments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="comments",
            field=models.ManyToManyField(
                blank=True, related_name="post_comments", to="comments.comment"
            ),
        ),
    ]