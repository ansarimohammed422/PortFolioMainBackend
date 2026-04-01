# Register your models here.
from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Certificate, Contact, Education, Experience, Project, Service, Skill

# @admin.register(Project)
# class ProjectAdmin(ModelAdmin):
#     list_display = ("title", "category", "frontend_id")
#     search_fields = ("title", "category")


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ("title", "category", "frontend_id")
    search_fields = ("title", "category")

    # Organizes the form into beautiful Libadwaita-style cards
    fieldsets = (
        ("Core Details", {"fields": ("frontend_id", "title", "category", "image")}),
        ("Documentation", {"fields": ("long_description", "tech_stack")}),
        ("External Links", {"fields": ("live_url", "github_url")}),
    )


@admin.register(Skill)
class SkillAdmin(ModelAdmin):
    list_display = ("name", "frontend_id", "order")
    list_editable = ("order",)
    ordering = ("order",)


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ("title", "icon", "frontend_id", "order")
    list_editable = ("order",)
    ordering = ("order",)


@admin.register(Experience)
class ExperienceAdmin(ModelAdmin):
    list_display = ("role", "company", "period", "frontend_id", "order")
    list_editable = ("order",)
    ordering = ("order",)


@admin.register(Education)
class EducationAdmin(ModelAdmin):
    list_display = ("degree", "institution", "period", "frontend_id", "order")
    list_editable = ("order",)
    ordering = ("order",)


@admin.register(Certificate)
class CertificateAdmin(ModelAdmin):
    list_display = ("title", "issuer", "method", "frontend_id", "order")
    list_editable = ("order",)
    ordering = ("order",)


@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ("name", "email", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email")
