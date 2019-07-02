from rest_framework import serializers

from .models import UserFav, UseFollow
from forums.models import ForumTopic
from users.models import UserProfile


class UserFavSerialzers(serializers.ModelSerializer):
    """用户收藏功能"""

    def validate(self, attrs):
        resu = UserFav.objects.filter(user_id=self.initial_data["user"], topic_id=int(self.initial_data["topic"]))
        if len(resu):
            raise serializers.ValidationError("您已经收藏过该帖子了")
        else:
            return attrs

    class Meta(object):
        model = UserFav
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    """用户"""
    class Meta(object):
        model = UserProfile
        fields = ("img_link", "username", "id")


class ForumTopicSerializer(serializers.ModelSerializer):
    """帖子内容"""
    author = UserSerializer()
    class Meta(object):
        model = ForumTopic
        fields = "__all__"


class UserFavRetriveSerialzers(serializers.ModelSerializer):
    """用户收藏序列化2"""
    topic = ForumTopicSerializer()

    class Meta(object):
        model = UserFav
        fields = "__all__"

    @classmethod
    def data_preloading(cls, queryset):
        queryset = queryset.prefetch_related("topic")
        return queryset


class UserFollowSerialzers(serializers.ModelSerializer):
    """用户关注功能"""

    class Meta(object):
        model = UseFollow
        fields = "__all__"


class UserFollowRetrieveSerialzers(serializers.ModelSerializer):
    """用户关注功能2"""
    follow = UserSerializer()
    user = UserSerializer()

    class Meta(object):
        model = UseFollow
        fields = "__all__"

    @classmethod
    def data_preloading(cls, queryset):
        queryset = queryset.prefetch_related("follow").prefetch_related("user")
        return queryset
