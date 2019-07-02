from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import throttling
from rest_framework_extensions.cache.mixins import CacheResponseMixin, ListCacheResponseMixin

from .models import Article, ArticleType, Person
from .serializers import ArticleHRJSerializers, ArticleTypeSerializer, ArticlePerSerializer, \
    Article_GR_Detail_Serializer, ArticleDetailSerializers
from utils.handle_cache import CacheKeyHandle


class CacheKeyHandleArticle(CacheKeyHandle, CacheResponseMixin):
    object_header_cache_key = "Article"
    list_header_cache_key = "Article"


class ListCacheKeyHandleArticle(CacheKeyHandle, ListCacheResponseMixin):
    object_header_cache_key = "Article"
    list_header_cache_key = "Article"


class Article_RM_Msgs(CacheKeyHandleArticle, viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    """获取国学入门的相关信息"""
    queryset = Article.objects.filter(article_type_id = 50)
    serializer_class = ArticleHRJSerializers

    # 用来对api访问进行限速的
    throttle_classes = (throttling.UserRateThrottle, throttling.AnonRateThrottle)

    # 定义缓存的键的开头
    object_cache_key = ":RM_Msg_retrive:"
    list_cache_key = ":RM_Msg_list:"


class Article_JR_Msgs(CacheKeyHandleArticle, viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    """获取今日国学的相关信息"""
    queryset = Article.objects.filter(article_type_id = 49)
    serializer_class = ArticleHRJSerializers

    throttle_classes = (throttling.UserRateThrottle, throttling.AnonRateThrottle)

    # 定义缓存的键的开头
    object_cache_key = ":JR_Msgs_retrive:"
    list_cache_key = ":JR_Msgs_list:"


class ArticleZWPage(PageNumberPagination):
    """分页的使用"""
    page_size = 8
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 10


class Article_ZW_Msgs(CacheKeyHandleArticle, viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """获取哲学文化的数据"""

    queryset = ArticleTypeSerializer.setup_eager_loading(ArticleType.objects.filter())
    serializer_class = ArticleTypeSerializer

    throttle_classes = (throttling.UserRateThrottle, throttling.AnonRateThrottle)

    # 定义缓存的键的开头
    object_cache_key = ":ZW_Msgs_retrive:"
    list_cache_key = ":ZW_Msgs_list:"


class Article_GR_Msgs(CacheKeyHandleArticle, viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """获取国学人物的数据"""

    queryset = ArticlePerSerializer.setup_eager_loading(ArticleType.objects.filter())
    serializer_class = ArticlePerSerializer

    throttle_classes = (throttling.UserRateThrottle, throttling.AnonRateThrottle)

    # 定义缓存的键的开头
    object_cache_key = ":GR_Msgs_retrive:"
    list_cache_key = ":GR_Msgs_list:"


class Article_GR_Detail_Msgs(CacheKeyHandleArticle, viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    """获取人物详情信息"""
    queryset = Article_GR_Detail_Serializer.setup_eager_loading(Person.objects.filter())
    serializer_class = Article_GR_Detail_Serializer

    throttle_classes = (throttling.UserRateThrottle, throttling.AnonRateThrottle)

    # 定义缓存的键的开头
    object_cache_key = ":GR_Detail_Msgs_retrive:"
    list_cache_key = ":GR_Detail_Msgs_list:"


class Article_Detail_Msgs(ListCacheKeyHandleArticle, viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    """获取文章的详细信息"""
    queryset = ArticleDetailSerializers.setup_eager_loading(Article.objects.all())
    serializer_class = ArticleDetailSerializers

    throttle_classes = (throttling.UserRateThrottle, throttling.AnonRateThrottle)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.browse_count += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # 定义缓存的键的开头
    object_cache_key = ":Detail_Msgs_retrive:"
    list_cache_key = ":Detail_Msgs_list:"
