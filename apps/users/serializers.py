from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import UserProfile


class UserIdSerializers(serializers.ModelSerializer):
    """获取用户id"""
    class Meta(object):
        model = UserProfile
        fields = ("id", )


class UserRegSerializer(serializers.ModelSerializer):
    """用户注册"""
    rpassword = serializers.CharField(
        required=True, write_only=True, label="确认密码", help_text="确认密码",
        error_messages={"required": "请输入密码"},
        style={'input_type': 'password'})

    password = serializers.CharField(
        required=True, style={'input_type': 'password'}, help_text="密码", label="密码",
        write_only=True, error_messages={"required": "请输入密码"},
    )
    username = serializers.CharField(
        required=True, help_text="用户名", label="用户名",
        error_messages={"required": "请输入用户名"},
        validators=[UniqueValidator(queryset=UserProfile.objects.all())],
    )
    email = serializers.CharField(
        required=True, help_text="邮箱", label="邮箱",
        error_messages={"required": "请输入邮箱"},
    )

    # def create(self, validated_data):
    #     """保存数据的时候就会调用这个方法"""
    #     user = super(UserRegSerializer, self).create(validated_data=validated_data)
    #     user.set_password(validated_data["password"])
    #     user.save()
    #     return user

    def validate(self, attrs):
        if attrs["password"] != attrs["rpassword"]:
            raise serializers.ValidationError("两次输入的密码不一致")
        del attrs["rpassword"]
        return attrs

    class Meta(object):
        model = UserProfile
        fields = ("username", "password", "rpassword", "email")


class UserInfoSerializers(serializers.ModelSerializer):
    """用户个人信息"""

    def validate(self, attrs):
        if "female" in attrs.values():
            attrs["gender"] = 'female'
        else:
            attrs["gender"] = 'male'
        return attrs

    class Meta(object):
        model = UserProfile
        fields = ("id", "username", "gender", "birthday","current_sort", "publish_post", "publish_reply", "total_grade", "email", "area", "introduce", "img_link", "name", "fans", "attention")