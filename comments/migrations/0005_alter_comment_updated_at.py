# Generated by Django 5.0.2 on 2024-03-28 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0004_alter_comment_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="updated_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
