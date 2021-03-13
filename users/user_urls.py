from django.urls import path, include
from rest_framework import routers

from users.views import *

router = routers.DefaultRouter()

router.register('get-user', GetUserViewset)
router.register('user', UserViewset)
router.register('admin-user', AdminUserViewset)

urlpatterns = [
    path('', include(router.urls))
]
