# """
# URL configuration for Portbackend project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/6.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """

# from django.contrib import admin
# from django.urls import include, path
# from rest_framework.routers import DefaultRouter

# from portfolio.views import (
#     CertificateViewSet,
#     ContactViewSet,
#     EducationViewSet,
#     ExperienceViewSet,
#     ProjectViewSet,
#     ServiceViewSet,
#     SkillViewSet,
# )

# router = DefaultRouter()
# router.register(r"projects", ProjectViewSet)
# router.register(r"skills", SkillViewSet)
# router.register(r"services", ServiceViewSet)
# router.register(r"experience", ExperienceViewSet)
# router.register(r"education", EducationViewSet)
# router.register(r"certificates", CertificateViewSet)
# router.register(r"contact", ContactViewSet)

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("api/v1/", include(router.urls)),
# ]

# backend/urls.py
from django.conf import settings  # Add this
from django.conf.urls.static import static  # Add this
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog.views import BlogViewSet  # <-- IMPORT THIS
from portfolio.views import (
    CertificateViewSet,
    ContactViewSet,
    EducationViewSet,
    ExperienceViewSet,
    ProjectViewSet,
    ServiceViewSet,
    SkillViewSet,
)

router = DefaultRouter()
router.register(r"projects", ProjectViewSet)
router.register(r"skills", SkillViewSet)
router.register(r"services", ServiceViewSet)
router.register(r"experience", ExperienceViewSet)
router.register(r"education", EducationViewSet)
router.register(r"certificates", CertificateViewSet)
router.register(r"contact", ContactViewSet)
router.register(r"blogs", BlogViewSet, basename="blog")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
]

# Add this block at the bottom to serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
