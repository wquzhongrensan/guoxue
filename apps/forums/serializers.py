from rest_framework import serializers

from .models import ForumType, ForumTopic, ForumContent, ForumReply
from users.models import UserProfile


class SubForumTypeSerializer(serializers.ModelSerializer):
    """序列化论坛分类2"""
    class Meta(object):
        model = ForumType
        fields = "__all__"


class ForumTypeSerializer(serializers.ModelSerializer):
    """序列化论坛分类1"""
    sub_forum = SubForumTypeSerializer(many=True)

    class Meta(object):
        model = ForumType
        fields = "__all__"

    @classmethod
    def setup_aeger_loading(cls, queryset):
        return queryset.prefetch_related("sub_forum")


class ForumTopicSerializer(serializers.ModelSerializer):
    """用户发帖"""

    content = serializers.CharField(required=True, write_only=True,
                                    error_messages={"required": "content字段不能为空"})

    def validate(self, attrs):
        del attrs["content"]
        return attrs

    class Meta(object):
        model = ForumTopic
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    """用户"""
    class Meta(object):
        model = UserProfile
        fields = ("username", "img_link")


class ForumReplySerializer(serializers.ModelSerializer):
    """用户回复"""
    author = AuthorSerializer()

    class Meta(object):
        model = ForumReply
        fields = "__all__"


class ForumContentSerializer(serializers.ModelSerializer):
    """用户回复"""

    class Meta(object):
        model = ForumContent
        fields = "__all__"


class ForumTopicDetailSerializer(serializers.ModelSerializer):
    """帖子内容"""

    forum_content = ForumContentSerializer(many=True)
    forum_reply = ForumReplySerializer(many=True)
    author = AuthorSerializer()


    class Meta(object):
        model = ForumTopic
        fields = "__all__"

    @classmethod
    def data_preloading(cls, queryset):
        queryset = queryset.select_related("author").prefetch_related("forum_content").prefetch_related("forum_reply")
        return queryset


class ForumReplySerializers(serializers.ModelSerializer):
    """用户回帖"""
    content = serializers.CharField(required=True)


    class Meta(object):
        model = ForumReply
        fields = "__all__"


class ForumTopicDetailForHonorSerializer(serializers.ModelSerializer):
    """帖子内容"""
    class Meta(object):
        model = ForumTopic
        fields = "__all__"


class ForumTopicDetailForHonorSerializer1(serializers.ModelSerializer):
    """帖子内容"""
    class Meta(object):
        model = ForumTopic
        fields = ("browse_count", "title")


class FormHonorSeralizers(serializers.ModelSerializer):
    """论坛荣誉榜"""
    author_forum = ForumTopicDetailForHonorSerializer1(many=True)

    class Meta(object):
        model = UserProfile
        fields = ["id", "author_forum", "username", "publish_post", "img_link", "total_grade"]

    @classmethod
    def data_preloading(cls, queryset):
        return queryset.prefetch_related("author_forum").filter(id__gt=1).order_by("-total_grade")[0:13]


class ForumTypeSerializerIndex(serializers.ModelSerializer):
    """序列化论坛分类2"""
    class Meta(object):
        model = ForumType
        fields = ("id", "title")


class ForumReplySerializerIndex(serializers.ModelSerializer):
    """用户回复"""
    author = AuthorSerializer()

    class Meta(object):
        model = ForumReply
        fields = ("id","author", "last_reply_time")


class ForumIndexDetailSerializer(serializers.ModelSerializer):
    """论坛首页帖子信息"""
    forum_type = ForumTypeSerializerIndex()
    forum_reply = ForumReplySerializerIndex(many=True)
    author = AuthorSerializer()

    class Meta(object):
        model = ForumTopic
        fields = "__all__"

    @classmethod
    def data_preloading(cls, queryset):
        queryset = queryset.select_related("forum_type").prefetch_related("forum_reply").prefetch_related("author")
        return queryset


class ForumIndexDetailSerializer1(serializers.ModelSerializer):
    """论坛首页帖子信息"""
    forum_type = ForumTypeSerializerIndex()
    author = AuthorSerializer()

    class Meta(object):
        model = ForumTopic
        fields = "__all__"


class ForumDetailReplySerializer(serializers.ModelSerializer):
    topic = ForumIndexDetailSerializer1()

    class Meta(object):
        model = ForumReply
        fields = ("topic", )

    @classmethod
    def data_preloading(cls, queryset):
        queryset = queryset.select_related("topic")
        return queryset


class ForumDetailSerializer(serializers.ModelSerializer):
    forum_content = ForumContentSerializer(many=True)

    class Meta(object):
        model = ForumTopic
        fields = "__all__"

    @classmethod
    def data_preloading(cls, queryset):
        queryset = queryset.prefetch_related("forum_content")
        return queryset
