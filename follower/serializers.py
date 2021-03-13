from rest_framework import serializers
from follower.models import Followers

class FollowerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Followers
    fields = (
      'id',
      'user',
      'follower'
    )
