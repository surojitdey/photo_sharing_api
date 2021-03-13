from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from users.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<id>/<filename>
    return '{0}/{1}'.format(instance.user.id, filename)

class Post(models.Model):
  user = models.ForeignKey(
      User, on_delete=models.CASCADE, related_name="post_user_id", to_field="id")
  added = models.DateTimeField(auto_now_add=True)
  media_file = models.FileField(upload_to=user_directory_path)

  def __str__(self):
    return self.user

class Like(models.Model):
  post = models.ForeignKey(
      Post, on_delete=models.CASCADE, related_name="like_post_id")
  user = models.ForeignKey(
      User, on_delete=models.CASCADE, related_name="liked_user_id", to_field="id")

class Comments(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment_post_id")
  user = models.ForeignKey(
      User, on_delete=models.CASCADE, related_name="comment_user_id", to_field="id")
  comment = models.TextField(_("comment"))
  comment_added = models.DateTimeField(auto_now_add=True)
