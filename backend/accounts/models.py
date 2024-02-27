from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):    
    username = models.CharField(
        max_length=32,
        unique=True,
        blank=False,
        null=False
    )
    
    profile_picture = models.ImageField(
        upload_to="profiles",
        blank=True,
        null=True
    )
    
    first_name = models.CharField(
        max_length=32,
        blank=False,
        null=False
    )
    
    last_name = models.CharField(
        max_length=32,
        blank=False,
        null=False
    )
    
    email = models.EmailField(
        blank=True,
        null=False
    )

    birthday = models.DateField(
        blank=True,
        null=True
    )
    
    country_code = models.IntegerField(
        blank=True,
        null=True
    )
    
    phone_number = models.CharField(
        max_length=16,
        blank=True,
        null=True
    )
    
    goverment_id = models.CharField(
        max_length=16,
        blank=True,
        null=True
    )
    
    address = models.CharField(
        max_length=32,
        blank=True,
        null=True
    )
    
    emergency_contact = models.CharField(
        max_length=16,
        blank=True,
        null=True
    )
    
    def __str__(self):
        return f"< {self.first_name} {self.last_name} | {self.email} >"
