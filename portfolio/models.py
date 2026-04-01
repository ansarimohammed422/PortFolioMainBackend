# Create your models here.
from django.db import models

# class Project(models.Model):
#     frontend_id = models.CharField(
#         max_length=50, unique=True, help_text="e.g., '1', '2'"
#     )
#     title = models.CharField(max_length=200)
#     category = models.CharField(max_length=100)
#     image_url = models.URLField(max_length=500)
#     tech_stack = models.JSONField(default=list, help_text='["React", "Tailwind"]')


#     def __str__(self):
#         return self.title
#


# class Project(models.Model):
#     frontend_id = models.CharField(
#         max_length=50, unique=True, help_text="e.g., '1', '2'"
#     )
#     title = models.CharField(max_length=200)
#     category = models.CharField(max_length=100)
#     # Changed from URLField to ImageField
#     image = models.ImageField(upload_to="projects/", blank=True, null=True)
#     tech_stack = models.JSONField(default=list, help_text='["React", "Tailwind"]')

#     def __str__(self):
#         return self.title


# class Project(models.Model):
#     frontend_id = models.CharField(
#         max_length=50, unique=True, help_text="e.g., '1', '2'"
#     )
#     title = models.CharField(max_length=200)
#     category = models.CharField(max_length=100)
#     image = models.ImageField(upload_to="projects/", blank=True, null=True)

#     # NEW: Long Description
#     long_description = models.TextField(
#         blank=True,
#         help_text="In-depth explanation of the project architecture and goals.",
#     )

#     # Existing links (ensure they look like this)
#     live_url = models.URLField(
#         blank=True, help_text="URL for the live deployed project"
#     )
#     github_url = models.URLField(
#         blank=True, help_text="URL for the source code repository"
#     )

#     tech_stack = models.JSONField(default=list, help_text='["React", "Django"]')

#     def __str__(self):
#         return self.title


class Project(models.Model):
    frontend_id = models.CharField(
        max_length=50, unique=True, help_text="e.g., '1', '2'"
    )
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    long_description = models.TextField(
        blank=True,
        help_text="In-depth explanation of the project architecture and goals.",
    )

    # CHANGED: From URLField to CharField to allow '#'
    live_url = models.CharField(
        max_length=500, blank=True, help_text="URL or '#' if not deployed"
    )
    github_url = models.CharField(
        max_length=500, blank=True, help_text="URL or '#' if private/not available"
    )

    tech_stack = models.JSONField(default=list, help_text='["React", "Django"]')

    def __str__(self):
        return self.title


class Skill(models.Model):
    frontend_id = models.CharField(max_length=50, unique=True, help_text="e.g., 's1'")
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Service(models.Model):
    frontend_id = models.CharField(max_length=50, unique=True, help_text="e.g., 'srv1'")
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(
        max_length=100, help_text="Lucide icon name, e.g., 'MonitorSmartphone'"
    )
    span = models.CharField(
        max_length=50, help_text="Tailwind class, e.g., 'md:col-span-2'"
    )
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Experience(models.Model):
    frontend_id = models.CharField(max_length=50, unique=True, help_text="e.g., 'exp1'")
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    period = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.role} at {self.company}"


class Education(models.Model):
    frontend_id = models.CharField(max_length=50, unique=True, help_text="e.g., 'edu1'")
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    period = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.degree


# class Certificate(models.Model):
#     frontend_id = models.CharField(
#         max_length=50, unique=True, help_text="e.g., 'react', 'django'"
#     )
#     method = models.CharField(max_length=10, default="GET")
#     title = models.CharField(max_length=200)
#     issuer = models.CharField(max_length=200)
#     period = models.CharField(max_length=100)
#     description = models.TextField()
#     tech = models.JSONField(default=list)
#     order = models.IntegerField(default=0)

#     def __str__(self):
#         return self.title


class Certificate(models.Model):
    frontend_id = models.CharField(
        max_length=50, unique=True, help_text="e.g., 'react', 'django'"
    )
    method = models.CharField(max_length=10, default="GET")
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    period = models.CharField(max_length=100)
    description = models.TextField()
    tech = models.JSONField(default=list)
    # Added ImageField for certificates
    image = models.ImageField(upload_to="certificates/", blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"
