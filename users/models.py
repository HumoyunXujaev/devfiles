from django.db import models

# Create your models here.
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    attempts = models.IntegerField(default=3)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)
    
    def decrease_attempts(self):
        if self.attempts > 0:
            self.attempts -= 1
            self.save()

    class Meta:
        ordering = ['created']
