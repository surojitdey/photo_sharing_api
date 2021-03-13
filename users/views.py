import json
from json import JSONEncoder
import re
import os

from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.conf import settings

from rest_framework import viewsets, status, permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserSerializer
from service_auth.permissions import IsAdminUser, IsUser, IsUserReadOnly


class GetUserViewset(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsUser]

  def get_queryset(self):
    return User.objects.filter(email=self.request.user)


class UserViewset(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsUser]

  def get_queryset(self):
    return User.objects.exclude(email=self.request.user)

  def get_permissions(self):
    if self.request.method == 'POST':
      self.permission_classes = (AllowAny,)

    return super(UserViewset, self).get_permissions()

  def create(self, request):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      if 'password' not in serializer.validated_data:
        return Response({'error': 'Password required'}, status=status.HTTP_400_BAD_REQUEST)
      user = User.objects.create_user(**serializer.validated_data)
      self.makedirs(settings.MEDIA_ROOT, user.id)

      return Response({'user': user.id}, status=status.HTTP_201_CREATED)
    return Response({'error': 'Some field is missing'}, status=status.HTTP_400_BAD_REQUEST)

  def perform_create(self, serializer):
    if 'password' in self.request.data:
      password = make_password(self.request.data['password'])
      serializer.save(password=password)
    else:
      serializer.save()

  def perform_update(self, serializer):
    if 'password' in self.request.data:
      password = make_password(self.request.data['password'])
      serializer.save(password=password)
    else:
      serializer.save()
  
  def makedirs(self, path, directory):
    path = os.path.join(path, str(directory))
    try:
        os.mkdir(path)
    except OSError as e:
        if e.errno == 17:
            # Dir already exists. No biggie.
            pass


class AdminUserViewset(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAdminUser]

  def get_permissions(self):
    if self.request.method == 'POST':
      self.permission_classes = (AllowAny,)

    return super(UserViewset, self).get_permissions()

  def create(self, request):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      if 'password' not in serializer.validated_data:
        return Response({'error': 'Password required'}, status=status.HTTP_400_BAD_REQUEST)
      user = User.objects.create_superuser(**serializer.validated_data)

      return Response({'user': user.id}, status=status.HTTP_201_CREATED)
    return Response({'error': 'Some field is missing'}, status=status.HTTP_400_BAD_REQUEST)

  def perform_create(self, serializer):
    if 'password' in self.request.data:
      password = make_password(self.request.data['password'])
      serializer.save(password=password)
    else:
      serializer.save()

  def perform_update(self, serializer):
    if 'password' in self.request.data:
      password = make_password(self.request.data['password'])
      serializer.save(password=password)
    else:
      serializer.save()

