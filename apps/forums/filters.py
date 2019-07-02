from django_filters import rest_framework as filters
from .models import ForumTopic, ForumReply


class ForumTopicFilter(filters.FilterSet):
    title_con = filters.CharFilter(field_name="title", lookup_expr='contains')
    forum_type_id = filters.CharFilter(field_name="forum_type_id", lookup_expr='exact')

    class Meta:
        model = ForumTopic
        fields = ['title_con', 'author', 'forum_type_id', "forum_reply"]


class ForumReplyFilter(filters.FilterSet):

    class Meta:
        model = ForumReply
        fields = ['author',]
