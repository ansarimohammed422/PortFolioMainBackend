from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Certificate, Contact, Education, Experience, Project, Service, Skill
from .serializers import (
    CertificateSerializer,
    ContactSerializer,
    EducationSerializer,
    ExperienceSerializer,
    ProjectSerializer,
    ServiceSerializer,
    SkillSerializer,
)


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all().order_by("id")  # Change order_by if needed
    serializer_class = ProjectSerializer


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all().order_by("order")
    serializer_class = SkillSerializer


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all().order_by("order")
    serializer_class = ServiceSerializer


class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Experience.objects.all().order_by("order")
    serializer_class = ExperienceSerializer


class EducationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Education.objects.all().order_by("order")
    serializer_class = EducationSerializer


class CertificateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Certificate.objects.all().order_by("order")
    serializer_class = CertificateSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ["post"]

    def perform_create(self, serializer):
        # 1. Save the contact message to the database first
        contact = serializer.save()

        # 2. Prepare the email content
        subject = f"New Portfolio Message from {contact.name}"
        message = (
            f"You have received a new message via your portfolio!\n\n"
            f"From: {contact.name}\n"
            f"Email: {contact.email}\n\n"
            f"Message:\n{contact.message}"
        )

        # 3. Send the email
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=True,  # Set to True in production so API doesn't crash if email fails
            )
        except Exception as e:
            # If the email fails (e.g., bad password), log it, but the DB save still worked
            print(f"Failed to send email notification: {e}")
