from django.db import models
from django.utils.translation import ugettext_lazy as _
from users.models import User

class Followers(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE,
                           related_name="user_id", to_field="id")
  follower = models.ManyToManyField(User)
