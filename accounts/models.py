from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        ROLE1 = "ROLE1", "Role1"
        ROLE2 = "ROLE2", "Role2"

    role = models.CharField(('Roles'), max_length=50, choices=Roles.choices, default=Roles.ROLE1)
    
class Role1(CustomUser):
    class Meta:
        proxy = True


class Role2(CustomUser):
    class Meta:
        proxy = True