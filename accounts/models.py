from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        ROLE1 = "ROLE1", "Role1"
        ROLE2 = "ROLE2", "Role2"

    role = models.CharField(('Roles'), max_length=50, choices=Roles.choices, default=Roles.ROLE1)
    
class Role1Manager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return super().get_queryset(*args,**kwargs).filter(role=CustomUser.Roles.ROLE1)

class Role1(CustomUser):
    objects = Role1Manager()
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = CustomUser.Roles.ROLE1
        return super().save(*args, **kwargs)


class Role2Manager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return super().get_queryset(*args,**kwargs).filter(role=CustomUser.Roles.ROLE2)

class Role2(CustomUser):
    objects = Role2Manager()
    class Meta:
        proxy = True

