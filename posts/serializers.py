from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from posts.models import *


class PostSerializer(serializers.ModelSerializer):
  user = serializers.SlugRelatedField(
      read_only=True,
      slug_field='id'
  )
  class Meta:
    model = Post
    fields = (
        'id',
        'user',
        'media_file'
    )


class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comments
    fields = (
      'id',
      'post',
      'user',
      'comment'
    )


class LikeSerializer(serializers.ModelSerializer):
  user = serializers.SlugRelatedField(
      read_only=True,
      slug_field='id'
  )
  class Meta:
    model = Like
    fields = (
      'id',
      'post',
      'user'
    )
