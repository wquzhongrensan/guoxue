import xadmin
from django.core.cache import cache

from .models import ForumType, ForumTopic, ForumContent, ForumReply


class ForumContentAdmin(object):
    list_display = ["id", "topic"]
    search_fields = ['topic',]
    list_editable = ["topic",]
    list_filter = ["topic", ]
    style_fields = {"content": "ueditor"}


class ForumTopicAdmin(object):
    list_display = ["id", "title"]
    search_fields = ['title', ]
    list_editable = ["title", ]
    list_filter = ["title", ]

    class ForumContentInline(object):
        model = ForumContent
        extra = 1
        style = 'tab'
        style_fields = {"content": "ueditor"}

    inlines = [ForumContentInline]


class BaseAdmins(object):
    object_key = "Forum*"
    list_key = "Forum*"

    def save_models(self):
        cache.delete_pattern(self.object_key)
        cache.delete_pattern(self.list_key)
        super().save_models()


class ForumTypeAdmin(BaseAdmins):
    list_display = ["id", "title", "forum_type", "parent_forum", ]
    search_fields = ['title', ]
    list_editable = ["title", ]
    list_filter = ["title", ]

    class ForumTopicInline(object):
        model = ForumTopic
        exclude = ["add_time"]
        extra = 1
        style = 'tab'

    inlines = [ForumTopicInline]


class ForumReplyAdmin(BaseAdmins):
    list_display = ["id", "author", "topic" ]
    search_fields = ['author',]
    list_editable = ["author", ]
    list_filter = ["author", ]
    style_fields = {"content": "ueditor"}


xadmin.site.register(ForumType, ForumTypeAdmin)
xadmin.site.register(ForumTopic, ForumTopicAdmin)
xadmin.site.register(ForumContent, ForumContentAdmin)
xadmin.site.register(ForumReply, ForumReplyAdmin)
