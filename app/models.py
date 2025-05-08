from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)  # ✅ Add this field
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):  # ✅ Inherit from PermissionsMixin
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  # ✅ Add this field

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

from multiselectfield import MultiSelectField

class Package(models.Model):
    MONTH_CHOICES = [
        ("Jan", "January"), ("Feb", "February"), ("Mar", "March"),
        ("Apr", "April"), ("May", "May"), ("Jun", "June"),
        ("Jul", "July"), ("Aug", "August"), ("Sep", "September"),
        ("Oct", "October"), ("Nov", "November"), ("Dec", "December"),
    ]

    place = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    price = models.FloatField()
    days = models.PositiveSmallIntegerField()
    nights = models.PositiveSmallIntegerField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    is_trending = models.BooleanField(default=False)

    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    image4 = models.ImageField(upload_to='images/')

    start_dates = models.JSONField(default=list)
    end_dates = models.JSONField(default=list)

    # Multi-select field for months
    months = MultiSelectField(choices=MONTH_CHOICES, max_length=50)

    days_plan = models.JSONField(default=list)
    total_person = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.place} - {self.country}"
