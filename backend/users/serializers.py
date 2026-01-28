# 将 Python 对象（模型）转换为 JSON 格式，供 API 返回；将 JSON 数据转换为 Python 对象，用于保存到数据库
from rest_framework import serializers
from django.contrib.auth.models import User

# 用户序列化器
# ModelSerializer	自动根据 Django 模型生成序列化字段
# model = User	指定使用 Django 内置的 User 模型
# fields	指定要序列化的字段
# read_only_fields = ['id']	id 字段只读，不允许前端修改
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']

# 注册序列化器
# write_only=True	密码只能写入，序列化时不返回（安全）
# min_length=6	密码最少 6 位
# create()	自定义创建用户的方法
# create_user(**validated_data)	使用 Django 的 create_user 方法，会自动对密码加密
# 为什么重写 create() 方法？

# 默认的 create() 方法不会对密码加密
# 使用 create_user() 会自动调用 Django 的密码哈希算法
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
