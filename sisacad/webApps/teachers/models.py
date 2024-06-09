from django.db import models

# Create your models here.
class Teacher(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField()
    names = models.CharField(max_length=255)
    lastnames = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=15)
    status = models.BooleanField(default=True)

    def _str_(self):
        return f"{self.names} {self.lastnames}"