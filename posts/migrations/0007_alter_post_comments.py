# Generated by Django 5.0.2 on 2024-03-28 14:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0002_remove_comment_post"),
        ("posts", "0006_alter_post_comments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="comments",
            field=models.ForeignKey(
                blank=True,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post_comments",
                to="comments.comment",
            ),
        ),
    ]
