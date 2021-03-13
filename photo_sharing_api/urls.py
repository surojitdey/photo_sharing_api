from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api-token-auth/', obtain_jwt_token),
    # path('api-token-refresh/', refresh_jwt_token),
    # path('api-token-verify/', verify_jwt_token),
    path('user-api/v-1/', include('users.user_urls'), name='user-api'),
    path('follower-api/v-1/', include('follower.follower_urls'), name='follower-api'),
    path('posts-api/v-1/', include('posts.post_urls'), name='posts-api'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
