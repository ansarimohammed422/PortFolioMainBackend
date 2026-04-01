from rest_framework import serializers

from .models import Certificate, Contact, Education, Experience, Project, Service, Skill

# class ProjectSerializer(serializers.ModelSerializer):
#     id = serializers.CharField(source="frontend_id", read_only=True)
#     img = serializers.URLField(source="image_url", read_only=True)
#     tech = serializers.JSONField(source="tech_stack", read_only=True)

#     class Meta:
#         model = Project
#         fields = ["id", "title", "category", "img", "tech"]


# class ProjectSerializer(serializers.ModelSerializer):
#     id = serializers.CharField(source="frontend_id", read_only=True)
#     # Automatically creates a full URL to the local image and maps it to 'img'
#     img = serializers.ImageField(source="image", read_only=True)
#     tech = serializers.JSONField(source="tech_stack", read_only=True)

#     class Meta:
#         model = Project
#         fields = ["id", "title", "category", "img", "tech"]


class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="frontend_id", read_only=True)
    img = serializers.ImageField(source="image", read_only=True)
    tech = serializers.JSONField(source="tech_stack", read_only=True)

    class Meta:
        model = Project
        # Added long_description, live_url, and github_url to the API response
        fields = [
            "id",
            "title",
            "category",
            "img",
            "tech",
            "long_description",
            "live_url",
            "github_url",
        ]


class SkillSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="frontend_id", read_only=True)

    class Meta:
        model = Skill
        fields = ["id", "name"]


class ServiceSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="frontend_id", read_only=True)
    desc = serializers.CharField(source="description", read_only=True)

    class Meta:
        model = Service
        fields = ["id", "title", "desc", "icon", "span"]


class ExperienceSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="frontend_id", read_only=True)
    desc = serializers.CharField(source="description", read_only=True)

    class Meta:
        model = Experience
        fields = ["id", "role", "company", "period", "desc"]


class EducationSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="frontend_id", read_only=True)
    desc = serializers.CharField(source="description", read_only=True)

    class Meta:
        model = Education
        fields = ["id", "degree", "institution", "period", "desc"]


# class CertificateSerializer(serializers.ModelSerializer):
#     id = serializers.CharField(source="frontend_id", read_only=True)
#     desc = serializers.CharField(source="description", read_only=True)
#     endpoint = serializers.SerializerMethodField()

#     class Meta:
#         model = Certificate
#         fields = [
#             "id",
#             "method",
#             "endpoint",
#             "title",
#             "issuer",
#             "period",
#             "desc",
#             "tech",
#         ]

#     def get_endpoint(self, obj):
#         # Dynamically formats the endpoint exactly as React expects it
#         if obj.method == "POST":
#             return f"/api/v1/verify/{obj.frontend_id}"
#         return f"/api/v1/certs/{obj.frontend_id}"


class CertificateSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="frontend_id", read_only=True)
    desc = serializers.CharField(source="description", read_only=True)
    endpoint = serializers.SerializerMethodField()
    # Map the certificate image if you want to use it in the UI later
    img = serializers.ImageField(source="image", read_only=True)

    class Meta:
        model = Certificate
        fields = [
            "id",
            "method",
            "endpoint",
            "title",
            "issuer",
            "period",
            "desc",
            "tech",
            "img",
        ]

    def get_endpoint(self, obj):
        if obj.method == "POST":
            return f"/api/v1/verify/{obj.frontend_id}"
        return f"/api/v1/certs/{obj.frontend_id}"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
