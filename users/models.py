from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

from .managers import CustomUserManager


class User(AbstractUser):
  class Role(models.TextChoices):
    ADMIN = 'admin', _('admin')
    USER = 'user', _('user')

  username = None
  ROLE = None
  email = models.EmailField(_('email address'), unique=True)
  role = models.CharField(_('user role'), max_length=15,
                          choices=Role.choices, default=Role.USER, blank=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = CustomUserManager()

  def __str__(self):
    return self.email

