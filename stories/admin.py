from django.contrib import admin

from stories.models import Story


class StoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user_id",
        "text",
        "content",
        "date_uploaded",
        "date_of_expiry",
    )

    ordering = ("date_uploaded", "date_of_expiry")


# Register your models here.
admin.site.register(Story, StoryAdmin)
