from django.urls import path, include
from rest_framework import routers

from posts.views import *

router = routers.DefaultRouter()

# router.register('get-user', GetUserViewset)
router.register('post', PostViewset)
router.register('like', LikeViewset)
router.register('comment', CommentViewset)

urlpatterns = [
    path('', include(router.urls))
]
