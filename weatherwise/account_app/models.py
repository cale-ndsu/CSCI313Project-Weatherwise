from django.db import models
import uuid  # Required for unique book instances

# Create your models here.
from django.urls import reverse  # To generate URLS by reversing URL patterns
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.contrib.auth.models import User

class Profile(models.Model):
    """Represents a user and the location they want associated with the account"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coordinates = models.CharField(max_length=1000)
    location_name = models.CharField(max_length=1000)

    def __str__(self):
        """String for representing the Profile object."""
        return f'{self.user},\n{self.coordinates},\n{self.location_name}'