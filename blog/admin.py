# Register your models here.
from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    # Unfold automatically styles these into a beautiful data table
    list_display = ("title", "is_published", "read_time", "published_date")

    # Creates a sleek filtering sidebar
    list_filter = ("is_published", "published_date")
    search_fields = ("title", "tags", "content")

    # Auto-fills the slug as you type the title
    prepopulated_fields = {"slug": ("title",)}

    # Unfold organizes these into distinct, card-like sections
    fieldsets = (
        (
            "Header Data",
            {"fields": ("title", "slug", "excerpt", "cover_image"), "classes": ["tab"]},
        ),
        (
            "Markdown Content",
            {
                "fields": ("content",),
                "description": "Paste your ChatGPT Markdown directly here. The React frontend will compile it.",
                "classes": ["tab"],
            },
        ),
        (
            "System Metadata",
            {"fields": ("tags", "read_time", "is_published"), "classes": ["tab"]},
        ),
    )
