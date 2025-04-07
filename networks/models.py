from django.db import models
from django.utils import timezone

# Create your models here.

class UserData(models.Model):
    first_name = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
     return f'{self.first_name} {self.last_name} {self.email} {self.created_date}'