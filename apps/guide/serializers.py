from rest_framework import serializers

from .models import GuideType, GuideDetail


class GuideTypeSerializer1(serializers.ModelSerializer):
    """指南分类信信息序列化"""
    class Meta(object):
        model = GuideType
        fields = ("id", "sub_guide", "title")


class GuideTypeSerializer(serializers.ModelSerializer):
    """指南分类信息序列化"""
    sub_guide = GuideTypeSerializer1(many=True)

    class Meta(object):
        model = GuideType
        fields = ("id", "sub_guide", "title")

    @classmethod
    def setup_eager_loading(cls, queryset):
        return queryset.prefetch_related("sub_guide")


class GuideDetailSerializer(serializers.ModelSerializer):
    """指南详情信息序列化"""
    guide_type = GuideTypeSerializer1()

    class Meta(object):
        model = GuideDetail
        fields = ("title", "link", "guide_type")

    @classmethod
    def setup_eager_loading(cls, queryset):
        return queryset.select_related("guide_type")
