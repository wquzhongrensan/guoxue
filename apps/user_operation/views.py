from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import UserFav, UseFollow
from users.models import UserProfile
from .serializers import UserFavSerialzers, UserFollowSerialzers, UserFavRetriveSerialzers, UserFollowRetrieveSerialzers

User = get_user_model()


class UserFavViewset(viewsets.GenericViewSet, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin):
    """用户收藏功能"""
    # queryset = UserFav.objects.all()
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('user', )

    def get_serializer_class(self):
        if self.action == "create":
            return UserFavSerialzers
        else:
            return UserFavRetriveSerialzers

    def get_queryset(self):
        if self.action == "create":
            return UserFav.objects.all()
        else:
            return UserFavRetriveSerialzers.data_preloading(UserFav.objects.all())

    def create(self, request, *args, **kwargs):

        data = request.data

        data["user"] = self.request.user.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        data1 = serializer.data
        data1["content"] = "收藏成功"

        headers = self.get_success_headers(serializer.data)
        return Response(data1, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()


class UserFollowViewset(viewsets.GenericViewSet, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    """用户关注功能"""
    # queryset = UseFollow.objects.all()
    # serializer_class = UserFollowSerialzers
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('user', 'follow')

    def get_serializer_class(self):
        if self.action == "create":
            return UserFollowSerialzers
        else:
            return UserFollowRetrieveSerialzers

    def get_queryset(self):
        if self.action == "create":
            return UseFollow.objects.all()
        else:
            return UserFollowRetrieveSerialzers.data_preloading(UseFollow.objects.all())

    def create(self, request, *args, **kwargs):

        data = request.data
        data["user"] = self.request.user.id
        if "user_name" in data:
            data["follow"] = User.objects.filter(username=data["user_name"])[0].id

        resu = UseFollow.objects.filter(user_id=int(data["user"]), follow_id=int(data["follow"]))
        if len(resu):
            return Response({
                "content": '您已经关注过该用户了'
            }, status=status.HTTP_200_OK)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        data1 = serializer.data
        data1["content"] = "关注成功"

        headers = self.get_success_headers(data1)
        return Response(data1, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
        # 修改用户的关注数
        user = self.request.user
        user.attention += 1
        user.save()
        # 修改用户的粉丝数
        user_follow = User.objects.filter(id=serializer.data['follow'])[0]
        user_follow.fans += 1
        user_follow.save()

    def perform_destroy(self, instance):
        # 修改用户的关注数
        user = self.request.user
        user.attention -= 1
        user.save()

        # 修改用户的粉丝数
        follow_id = int(instance.follow_id)
        user_follow = UserProfile.objects.filter(id=follow_id)[0]
        user_follow.fans -= 1
        user_follow.save()

        instance.delete()
