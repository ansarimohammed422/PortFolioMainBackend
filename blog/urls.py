from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BlogViewSet

router = DefaultRouter()
# ... your other registered routes (skills, projects, etc)
router.register(r"blogs", BlogViewSet, basename="blog")

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
