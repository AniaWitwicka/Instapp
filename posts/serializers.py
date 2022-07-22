from .models import Post, Photo
from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(obj.id)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "caption",
            "date",
            "is_carousel_item",
            "location_id",
            "media_type",
            "status",
            "thumb_offset",
            "access_token",
            "ig_user_id"
        )


class PhotoSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(obj.id)

    class Meta:
        model = Photo
        fields = (
            "id",
            "title",
            "url",
            "post"
        )
