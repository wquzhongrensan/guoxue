from datetime import datetime

from urllib.parse import urlsplit
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework import throttling
from django_filters.rest_framework import DjangoFilterBackend

from .models import ForumType, ForumTopic, ForumContent, ForumReply
from users.models import UserProfile
from .serializers import ForumTypeSerializer, ForumTopicSerializer, \
    ForumTopicDetailSerializer, ForumReplySerializers, FormHonorSeralizers,\
    ForumIndexDetailSerializer, ForumDetailReplySerializer, ForumDetailSerializer
from utils.handle_cache import CacheKeyHandle


class CacheKeyHandleForum(CacheKeyHandle, CacheResponseMixin):
    object_header_cache_key = "Forum"
    list_header_cache_key = "Forum"


class ForumTypeMsgs(CacheKeyHandleForum, viewsets.GenericViewSet, mixins.RetrieveModelMixin ,mixins.ListModelMixin):
    """获取论坛分类信息"""
    queryset = ForumTypeSerializer.setup_aeger_loading(ForumType.objects.filter(forum_type=1))
    serializer_class = ForumTypeSerializer

    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    # 用来对api访问进行限速的
    throttle_classes = (throttling.UserRateThrottle, throttling.AnonRateThrottle)

    # 定义缓存的键的开头
    object_cache_key = ":TypeMsgs_retrive:"
    list_cache_key = ":TypeMsgs_list:"


class ForumCreateTopicViewsets(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """用户发帖"""
    queryset = ForumTopic.objects.all()
    serializer_class = ForumTopicSerializer

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):

        data = request.data

        # 不要在这里校验字段，把字段校验放到serializer中
        # if not data.get("content",''):
        #     return Response({
        #         "content": 'content字段不能为空'
        #     }, status=status.HTTP_400_BAD_REQUEST)

        data["author"] = str(UserProfile.objects.filter(username=data["author"])[0].id)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        forum_topic = self.perform_create(serializer)

        # 这一部分是在构造响应报文的
        re_dict = serializer.data

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        # 获取forum_topic对象
        forum_topic = serializer.save()

        # 保存帖子内容信息
        forum_content = ForumContent()
        forum_content.topic = forum_topic
        forum_content.content = self.request.data.get("content",'')
        forum_content.save()

        # 修改用户的发帖信息
        user = self.request.user
        user.publish_post += 1
        user.total_grade += 5
        user.save()

        users = UserProfile.objects.all().order_by('-total_grade')
        paiming = 0
        for i, userss in enumerate(users):
            if userss.id == user.id:
                paiming = i
                break
        user.current_sort = int(paiming + 1)
        user.save()

        return forum_topic


class ForumTopicDetailViewsets(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """帖子详情信息"""
    queryset = ForumTopicDetailSerializer.data_preloading(ForumTopic.objects.all())
    serializer_class = ForumTopicDetailSerializer

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # 用来对api访问进行限速的
    throttle_classes = (throttling.UserRateThrottle, throttling.AnonRateThrottle)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.browse_count += 1
        instance.save()
        serializer = self.get_serializer(instance)

        re_dict = serializer.data
        re_dict["reply_count"] = len(re_dict["forum_reply"])

        # 获得当前的HTTP或HTTPS
        http = urlsplit(self.request.build_absolute_uri(None)).scheme
        # 获取当前域名
        host = self.request.META['HTTP_HOST']
        total_host = http + '://' + host
        # replace_url = os.path.join(total_host, "media")
        replace_url = total_host + "/media/"

        content = re_dict["forum_content"][0]["content"].replace("/media", replace_url)

        re_dict["forum_content"][0]["content"] = content

        return Response(re_dict)


class ForumReplyViewsets(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """用户回帖"""
    queryset = ForumReply
    serializer_class = ForumReplySerializers
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)


    def create(self, request, *args, **kwargs):
        data = request.data

        data["author"] = str(UserProfile.objects.filter(username=data["author"])[0].id)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        forum_topic = self.perform_create(serializer)

        # 这一部分是在构造响应报文的
        re_dict = serializer.data
        user_data = UserProfile.objects.filter(id=int(re_dict['author']))[0]

        # 获得当前的HTTP或HTTPS
        http = urlsplit(self.request.build_absolute_uri(None)).scheme
        # 获取当前域名
        host = self.request.META['HTTP_HOST']
        total_host = http + '://' + host
        replace_url = total_host + "/media/"

        re_dict['author'] = {"img_link": replace_url+user_data.img_link.name, "username": user_data.username}

        headers = self.get_success_headers(re_dict)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        # 获取forum_topic对象
        forum_reply = serializer.save()

        # 修改帖子的最后回复时间
        forum_topic = ForumTopic.objects.filter(id=forum_reply.topic_id)[0]
        forum_topic.last_reply_time = datetime.now()
        forum_topic.save()
        # 修改用户发帖信息
        user = self.request.user
        user.publish_reply += 1
        user.total_grade += 3
        user.save()

        users = UserProfile.objects.all().order_by('-total_grade')
        paiming = 0
        for i, userss in enumerate(users):
            if userss.id == user.id:
                paiming = i
                break
        user.current_sort = int(paiming+1)
        user.save()

        return forum_reply


class ForumHonorViewsets(viewsets.GenericViewSet, mixins.ListModelMixin):
    """展示荣誉榜信息"""
    queryset = FormHonorSeralizers.data_preloading(UserProfile.objects.all())
    serializer_class = FormHonorSeralizers

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # 用来对api访问进行限速的
    throttle_classes = (throttling.UserRateThrottle, throttling.AnonRateThrottle)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)

        data = serializer.data

        # 自定义返回的信息
        data_person = []
        for each in data:
            forum_dict = dict(each)
            each_person = []
            each_forum = forum_dict["author_forum"]
            for each in each_forum:
                each_person.append(dict(each))
            each_list22 = sorted(each_person, key=lambda each_person: each_person["browse_count"])[-1: len(each_person)]
            forum_dict["author_forum"] = each_list22
            data_person.append(forum_dict)

        return Response(data_person)


class LargeResultsSetPagination(PageNumberPagination):
    """分页内容的基本配置"""
    page_size = 7
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class ForumIndexDetail(mixins.ListModelMixin,  viewsets.GenericViewSet, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    """论坛帖子信息"""
    queryset = ForumTopic.objects.all().order_by('pk')
    serializer_class = ForumIndexDetailSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    from .filters import ForumTopicFilter
    filter_class = ForumTopicFilter
    search_fields = ('title',)
    ordering_fields = ('id', 'browse_count')

    # 用来对api访问进行限速的
    throttle_classes = (throttling.UserRateThrottle, throttling.AnonRateThrottle)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)

            data = serializer.data
            # 自定义返回的信息
            data_forum = []
            for each in data:
                forum_dict = dict(each)
                forum_dict["reply_count"] = len(forum_dict["forum_reply"])
                reply_list = forum_dict["forum_reply"]
                temp_list = sorted(reply_list, key=lambda reply_list : reply_list["last_reply_time"])[-1: len(reply_list)]
                forum_dict["forum_reply"] = temp_list[0]["author"]["username"] if temp_list else ''
                data_forum.append(forum_dict)
            return self.get_paginated_response(data_forum)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


class ForumDetailReply(CacheKeyHandleForum, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """获取用户回帖的信息"""
    queryset = ForumDetailReplySerializer.data_preloading(ForumReply.objects.filter().order_by('pk'))
    serializer_class = ForumDetailReplySerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = (DjangoFilterBackend, )

    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    from .filters import ForumReplyFilter
    filter_class = ForumReplyFilter

    # 用来对api访问进行限速的
    throttle_classes = (throttling.UserRateThrottle, throttling.AnonRateThrottle)

    # 定义缓存的键的开头
    object_cache_key = ":DetailReply_retrive:"
    list_cache_key = ":DetailReply_list:"


class ForumDetail(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = ForumDetailSerializer.data_preloading(ForumTopic.objects.filter().order_by('pk'))
    serializer_class = ForumDetailSerializer
    pagination_class = LargeResultsSetPagination
