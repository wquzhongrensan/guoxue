from rest_framework import serializers
from .models import BookAuthor, BookDetail, BookType


class BookAuthorSerializer(serializers.Serializer):
    """图片会自动加上media目录"""
    name = serializers.CharField(required=True, max_length=100)
    avatar_link = serializers.ImageField()
    introduces = serializers.CharField(max_length=300)


class BookAuthorModelSerializer(serializers.ModelSerializer):
    """使用modelserializer会自动带上id，而且图片会自动加上域名"""

    class Meta(object):
        model = BookAuthor
        fields = "__all__"


class BookModelSerializer(serializers.ModelSerializer):
    """"""
    author = BookAuthorModelSerializer()
    class Meta(object):
        model = BookDetail
        fields = ["author", "name", "catalog"]


class BookTypeModelSerializer_sub1(serializers.ModelSerializer):
    """书籍子分类"""
    class Meta(object):
        model = BookType
        fields = "__all__"

from rest_framework_extensions.serializers import (
    PartialUpdateSerializerMixin
)


class BookDetailSerializer(PartialUpdateSerializerMixin, serializers.ModelSerializer):
    """获取指定类别的所有书籍信息"""
    author = BookAuthorModelSerializer()

    class Meta(object):
        model = BookDetail
        fields = "__all__"

    @classmethod
    def setup_eager_loading(cls, queryset):
        return queryset.select_related("author")


class BookDetailATSerializer(serializers.ModelSerializer):
    """获取数据分类信息以及书籍的详情信息"""
    sub_book = BookTypeModelSerializer_sub1(many = True)
    book = BookDetailSerializer(many=True)

    class Meta(object):
        model = BookType
        fields = "__all__"

    @classmethod
    def setup_eager_loading(cls, queryset):
        queryset = queryset.prefetch_related('book')
        queryset = queryset.prefetch_related('sub_book')

        return queryset


class BookHomepageSerializer(PartialUpdateSerializerMixin, serializers.ModelSerializer):
    """序列化首页的书籍信息"""

    class Meta(object):
        model = BookDetail
        fields = ["id", "img_link", "desc", "name"]
