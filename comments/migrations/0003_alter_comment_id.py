# Generated by Django 5.0.2 on 2024-03-28 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0002_remove_comment_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]