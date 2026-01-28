# 视图函数
# 视图类就是处理 HTTP 请求并返回 HTTP 响应的控制器
# 处理 HTTP 请求，返回 HTTP 响应。


from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer, RegisterSerializer

# 注册视图
# CreateAPIView	继承自 DRF 的通用视图，专门处理 POST 请求（创建资源）
# queryset	查询集，指明操作的模型
# serializer_class	使用的序列化器
# permission_classes = [permissions.AllowAny]	允许任何人访问（注册不需要登录）
class RegisterView(generics.CreateAPIView):
    # 自动接收 POST 请求
    # 自动处理数据解析（JSON / Form Data）
    # 1. 将请求的 JSON 数据传给序列化器
    # 2. 验证数据是否合法（用户名是否重复、密码长度等）
    # 3. 如果验证失败，返回错误信息
    # 4. 如果验证成功，调用 create() 保存数据
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


# 用户资料视图
# RetrieveUpdateAPIView	支持 GET（获取）和 PUT/PATCH（更新）请求
# permission_classes = [permissions.IsAuthenticated]	必须登录才能访问
# get_object()	返回当前登录用户
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user
