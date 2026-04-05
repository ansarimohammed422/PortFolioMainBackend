from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Blog
from .serializers import BlogSerializer


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Retrieves the list of published blogs.
    """

    serializer_class = BlogSerializer
    lookup_field = "slug"  # Allows fetching by URL slug instead of ID

    def get_queryset(self):
        # Only return blogs that are marked as published
        return Blog.objects.filter(is_published=True).order_by("-published_date")
