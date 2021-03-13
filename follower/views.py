import json
from json import JSONEncoder

from django.shortcuts import render
from django.contrib.auth.hashers import make_password

from rest_framework import viewsets, status, permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.views import APIView

from follower.models import Followers
from follower.serializers import FollowerSerializer
from service_auth.permissions import IsAdminUser, IsUser, IsUserReadOnly
from users.models import User


class FollowerViewset(viewsets.ModelViewSet):
  queryset = Followers.objects.all()
  serializer_class = FollowerSerializer
  permission_classes = [IsUser]

  def get_queryset(self):
    return Followers.objects.filter(user=self.request.user)
  
  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

