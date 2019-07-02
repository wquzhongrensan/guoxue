from rest_framework import serializers

from .models import Article, ArticleContent, ArticleType, Person, PersonContent


class ArticleHRJSerializers(serializers.ModelSerializer):
    """序列化国学入门和今日国学的article"""
    class Meta(object):
        model = Article
        fields = ["id", "title"]


class ArticleSerializers(serializers.ModelSerializer):
    """序列化article"""
    class Meta(object):
        model = Article
        fields = "__all__"


class ArticleTypeSerializer2(serializers.ModelSerializer):
    """序列化文章类别信息"""
    class Meta(object):
        model = ArticleType
        fields = "__all__"


class ArticleTypeSerializer1(serializers.ModelSerializer):
    """序列化文章类别信息"""
    # sub_acticle = ArticleTypeSerializer2(many=True)

    class Meta(object):
        model = ArticleType
        fields = "__all__"


class ArticleTypeSerializer(serializers.ModelSerializer):
    """序列化文章类别信息"""
    sub_acticle = ArticleTypeSerializer1(many=True)
    article = ArticleSerializers(many=True)

    class Meta(object):
        model = ArticleType
        fields = "__all__"

    @classmethod
    def setup_eager_loading(cls, queryset):
        queryset = queryset.prefetch_related("sub_acticle").prefetch_related("article")
        return queryset


class PersonSerializer(serializers.ModelSerializer) :
    """序列化人物详情"""
    class Meta(object):
        model = Person
        fields = "__all__"


class ArticlePerSerializer(serializers.ModelSerializer):
    """序列化人物信息"""
    sub_acticle = ArticleTypeSerializer1(many=True)
    person = PersonSerializer(many=True)

    class Meta(object):
        model = ArticleType
        fields = "__all__"

    @classmethod
    def setup_eager_loading(cls, queryset):
        queryset = queryset.prefetch_related("sub_acticle").prefetch_related("person")
        return queryset


class Article_GR_Detail_Person_Serializer(serializers.ModelSerializer):
    """序列化人物介绍详情"""
    class Meta(object):
        model = PersonContent
        fields = "__all__"


class Article_GR_Detail_Serializer(serializers.ModelSerializer) :
    """序列化人物详情"""
    person_content = Article_GR_Detail_Person_Serializer(many=True)
    class Meta(object):
        model = Person
        fields = "__all__"

    @classmethod
    def setup_eager_loading(cls, queryset):
        queryset = queryset.prefetch_related("person_content")
        return queryset


class ArticleContentSerializer(serializers.ModelSerializer):
    """序列化文章详情内容"""
    class Meta(object):
        model = ArticleContent
        fields = "__all__"


class ArticleDetailSerializers(serializers.ModelSerializer):
    """序列化article的所有信息"""
    article_content = ArticleContentSerializer(many=True)

    class Meta(object):
        model = Article
        fields = "__all__"

    @classmethod
    def setup_eager_loading(cls, queryset):
        return queryset.prefetch_related("article_content")
