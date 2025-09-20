from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager, BaseUserManager


class CustomUserManager(UserManager):
    def _create_user(self, phone_number, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not specified a valid e-mail address")

        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_user(self, phone_number=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, email, password, **extra_fields)

    def create_superuser(self, phone_number=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(phone_number, email, password, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email


class Files(models.Model):
    file = models.FileField(upload_to='filefolder/', null=True, blank=False)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name='fileowner')
    extension = models.CharField(max_length=255, null=True, blank=True)
    file_size = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Package(models.Model):
    name = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    cost = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
