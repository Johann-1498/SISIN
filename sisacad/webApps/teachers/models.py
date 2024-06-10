from django.db import models
import uuid

# Create your models here.
class Teacher(models.Model):
    """id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)"""
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField()
    names = models.CharField(max_length=255)
    lastnames = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=15)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.names} {self.lastnames}"