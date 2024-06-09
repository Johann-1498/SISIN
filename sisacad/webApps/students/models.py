from django.db import models
import uuid

# Create your models here.

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cui = models.CharField(max_length=8, unique=True)
    names = models.CharField(max_length=50)
    lastnames = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.lastnames} {self.names}"