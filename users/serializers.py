from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)
  class Meta:
    model = User
    fields = (
      'id',
      'password',
      'first_name',
      'last_name',
      'role',
      'email'
    )
    extra_kwargs = {
      'password': { 'write_only': True }
    }
