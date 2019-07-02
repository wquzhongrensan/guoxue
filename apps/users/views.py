from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import redirect
# from django.views.generic import View
from rest_framework import mixins, viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework import filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from django.views.generic.base import View
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from django.conf import settings

from .models import UserProfile
from .serializers import UserRegSerializer, UserInfoSerializers, UserIdSerializers
from .filters import UserFilter
from .task import send_mail_confirms

User = get_user_model()


class UserAuthBackend(ModelBackend):
    """
    自定义用户认证
    这个方法就是再用户登录时会调用来进行验证的，在生成token信息时也会调用
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 可以指定手机号或者用户名来进行认证
            # user = User.objects.get(Q(username=username)|Q(mobile=username))
            user = User.objects.get(Q(username=username))
            if user.check_password(password):
                return user
        except Exception as result:
            return None


class UserRegViewsets(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """用户注册功能"""
    queryset = UserProfile.objects.all()
    serializer_class = UserRegSerializer

    # 通过这个来自定义返回的内容
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        # payload = jwt_payload_handler(user)
        # re_dict["token"] = jwt_encode_handler(payload)
        # re_dict["username"] = user.name if user.name else user.username
        # re_dict["user_id"] = user.id

        confirm_serializer = Serializer(settings.SECRET_KEY, 3600)

        token = confirm_serializer.dumps({"user_id": user.id}).decode("utf-8")

        # 发送账号激活邮件，激活用户账号
        send_mail_confirms.delay(token, user.email, user.username)

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):

        instance = serializer.save()
        instance.current_sort = len(UserProfile.objects.all())
        instance.is_active = False

        password = instance.password
        instance.set_password(password)

        instance.save()

        return instance


class UserConfirmViewset(View):
    """用户账号确认相关的"""
    def get(self, request, token):
        """确认token信息"""
        confirm_serializer = Serializer(settings.SECRET_KEY, 3600)
        user_info = confirm_serializer.loads(token)
        # 激活用户信息
        user_id = user_info["user_id"]
        user = User.objects.filter(id=user_id)[0]
        user.is_active = True
        user.save()

        return redirect("/")


class UserInfoViewsets(viewsets.GenericViewSet, mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin, mixins.ListModelMixin):
    """用户个人信息"""
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.all()
    serializer_class = UserInfoSerializers
    filter_backends = (DjangoFilterBackend, )
    filter_class = UserFilter


class UserIDInfo(viewsets.GenericViewSet,mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    """获取用户个人信息"""
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.filter()
    serializer_class = UserInfoSerializers
    filter_backends = (DjangoFilterBackend,)

    from .filters import UserFilter
    filter_class = UserFilter


class UserId(viewsets.GenericViewSet,mixins.ListModelMixin):
    """获取用户的user_id"""
    queryset = UserProfile.objects.filter()
    serializer_class = UserIdSerializers
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('username', )

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class UserLoginThirdparty(View):
    """
    用户第三方认证回调
    """
    def get(self, request):
        re_dict = {}
        re_dict["token"] = request.COOKIES.get("token", None)
        re_dict["username"] = request.COOKIES.get("username", None)
        re_dict["user_id"] = request.COOKIES.get("user_id", None)
        return JsonResponse(re_dict, safe=False)
