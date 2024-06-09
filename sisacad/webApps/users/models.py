from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def _str_(self):
        return self.user_name