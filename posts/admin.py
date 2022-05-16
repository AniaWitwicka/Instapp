from django.contrib import admin
from .models import Post, Photo


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "owner",
        "is_posted",
        "date",
    )
    list_filter = ("title", "owner", "is_posted")
    search_fields = ("title", "owner")
    ordering = ("-id",)


admin.site.register(Post, PostAdmin)


class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "post",
    )
    list_filter = ("title", "post")
    search_fields = ("title", "post")
    ordering = ("-id",)


admin.site.register(Photo, PhotoAdmin)