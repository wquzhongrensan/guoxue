from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework_extensions.cache.mixins import CacheResponseMixin, ListCacheResponseMixin
from rest_framework import throttling

from .models import BookType, BookDetail
from .serializers import BookDetailATSerializer, BookDetailSerializer, BookHomepageSerializer
from utils.handle_cache import CacheKeyHandle


class BookDetailATPagination(PageNumberPagination):
    """分页配置"""
    page_size = 3
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 10


class CacheKeyHandleBook(CacheKeyHandle, CacheResponseMixin):
    object_header_cache_key = "Book"
    list_header_cache_key = "Book"


class ListCacheKeyHandleArticle(CacheKeyHandle, ListCacheResponseMixin):
    object_header_cache_key = "Book"
    list_header_cache_key = "Book"


class BookTypeMsgs(CacheKeyHandleBook, CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    书籍分类信息
    """
    queryset = BookDetailATSerializer.setup_eager_loading(queryset=BookType.objects.all())
    serializer_class = BookDetailATSerializer
    pagination_class = BookDetailATPagination

    # 用来对api访问进行限速的
    throttle_classes = (throttling.UserRateThrottle, throttling.AnonRateThrottle)

    # 定义缓存的键的开头
    object_cache_key = ":type_retrive:"
    list_cache_key = ":type_list:"


class BookDetailMsgs(ListCacheKeyHandleArticle, CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """书籍详细信息"""
    # queryset = BookDetail.objects.all()
    queryset = BookDetailSerializer.setup_eager_loading(BookDetail.objects.all())
    serializer_class = BookDetailSerializer
    # 用来对api访问进行限速的
    throttle_classes = (throttling.UserRateThrottle, throttling.AnonRateThrottle)

    # 定义缓存的键的开头
    object_cache_key = ":detail_retrive:"
    list_cache_key = ":detail_list:"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.browse_count += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class BookHomepages(CacheKeyHandleBook, CacheResponseMixin, mixins.ListModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    """获取首页的书籍信息"""
    queryset = BookDetail.objects.all().order_by('id')[0:4]
    serializer_class = BookHomepageSerializer
    # 用来对api访问进行限速的
    throttle_classes = (throttling.UserRateThrottle, throttling.AnonRateThrottle)

    # 定义缓存的键的开头
    object_cache_key = ":homepage_retrive:"
    list_cache_key = ":homepage_list:"


class BookSortHomepages(CacheKeyHandleBook, mixins.ListModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    """获取首页的书籍信息"""
    queryset = BookDetail.objects.all().order_by('browse_count')[0:6]
    serializer_class = BookHomepageSerializer
    # 用来对api访问进行限速的
    throttle_classes = (throttling.UserRateThrottle, throttling.AnonRateThrottle)

    # 定义缓存的键的开头
    object_cache_key = ":sorthomepage_retrive:"
    list_cache_key = ":sorthomepage_list:"
