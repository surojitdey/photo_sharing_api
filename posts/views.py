import json
from json import JSONEncoder
import re
import os

from django.shortcuts import render
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
from rest_framework.parsers import FormParser, MultiPartParser

from users.models import User
from posts.models import Post, Comments, Like
from posts.serializers import PostSerializer, CommentSerializer, LikeSerializer
from service_auth.permissions import IsAdminUser, IsUser, IsUserReadOnly


class PostViewset(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = [IsUser]
  parser_classes = (MultiPartParser, FormParser,)

  def get_queryset(self):
    return Post.objects.filter(user=self.request.user.id)
  
  def perform_create(self, serializer):
    serializer.save(user=self.request.user,
                    media_file=self.request.data.get('media_file'))



class CommentViewset(viewsets.ModelViewSet):
  queryset = Comments.objects.all()
  serializer_class = CommentSerializer
  permission_classes = [IsUser]

  # def get_queryset(self):
  #   if self.request.method == 'GET':
  #     return Like.objects.filter(post=self.request.query_params['pid'])


class LikeViewset(viewsets.ModelViewSet):
  queryset = Like.objects.all()
  serializer_class = LikeSerializer
  permission_classes = [IsUser]

  def get_queryset(self):
    if self.request.method == 'GET':
      return Like.objects.filter(post=self.request.query_params['pid'])
  
  def perform_create(self, serializer):
    post_instance = Post.objects.get(id=self.request.data.get('post'))
    if Like.objects.filter(post=post_instance):
      self.perform_destroy(Like.objects.get(post=post_instance))
    else:
      serializer.save(user=self.request.user, post=post_instance)
  
  def perform_destroy(self, instance):
    instance.delete()
