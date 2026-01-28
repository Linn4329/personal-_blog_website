# 路由配置
# /register/	RegisterView	用户注册
# /login/	TokenObtainPairView	登录获取 JWT Token
# /token/refresh/	TokenRefreshView	刷新过期的 access_token
# /profile/	UserProfileView	获取/更新当前用户信息
# JWT Token 机制：

# access_token：短期有效（如 30 分钟），用于访问 API
# refresh_token：长期有效（如 7 天），用于刷新 access_token
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
