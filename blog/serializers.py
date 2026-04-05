from rest_framework import serializers

from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    tag_list = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "slug",
            "excerpt",
            "content",
            "cover_image",
            "tag_list",
            "read_time",
            "published_date",
        ]

    def get_tag_list(self, obj):
        # Converts "React, Django, API" into ["React", "Django", "API"]
        if obj.tags:
            return [tag.strip() for tag in obj.tags.split(",")]
        return []
