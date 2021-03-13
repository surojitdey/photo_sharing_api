from django.urls import path, include
from rest_framework import routers

from follower.views import FollowerViewset

router = routers.DefaultRouter()

router.register('user-follower', FollowerViewset)

urlpatterns = [
    path('', include(router.urls))
]
