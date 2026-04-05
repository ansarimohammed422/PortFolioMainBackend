# Create your models here.
from django.db import models
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    excerpt = models.TextField(help_text="Short description for the blog card")

    # This is where you paste the ChatGPT Markdown text
    content = models.TextField(help_text="Paste Markdown content here")

    cover_image = models.URLField(
        max_length=500, blank=True, help_text="Image URL from Unsplash or Imgur"
    )
    tags = models.CharField(
        max_length=200, help_text="Comma-separated tags (e.g. React, Django, API)"
    )

    read_time = models.PositiveIntegerField(
        help_text="Estimated read time in minutes", default=5
    )
    is_published = models.BooleanField(default=True)
    published_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-published_date"]  # Newest first

    def save(self, *args, **kwargs):
        # Auto-generate slug from title if it's empty
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
