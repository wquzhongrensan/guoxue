import xadmin
from django.core.cache import cache

from .models import BookType, BookAuthor, BookDetail
from .views import BookTypeMsgs, BookDetailMsgs


class BaseAdmins(object):

    object_key = "Book*"
    list_key = "Book*"

    def save_models(self):
        cache.delete_pattern(self.object_key)
        cache.delete_pattern(self.list_key)
        super().save_models()


class BookTypeAdmin(BaseAdmins):

    list_display = ["id", "title", "desc", "book_type", "parent_forum", ]
    search_fields = ['title', ]
    list_editable = ["title", ]
    list_filter = ["title", ]

    object_key = BookTypeMsgs.object_header_cache_key + "*"
    list_key = BookTypeMsgs.list_header_cache_key + "*"


class BookAuthorAdmin(BaseAdmins):
    list_display = ["id", "name", "introduce_link", "introduces", "avatar_link"]
    search_fields = ['name', ]
    list_editable = ["name", ]
    list_filter = ["name", ]

    object_key = BookDetailMsgs.object_header_cache_key + "*"
    list_key = BookDetailMsgs.list_header_cache_key + "*"

    class BookDetailInline(BaseAdmins):
        model = BookDetail
        exclude = ["add_time"]
        extra = 1
        style = 'tab'
        style_fields = {"catalog": "ueditor"}

    inlines = [BookDetailInline]


class BookDetailAdmin(BaseAdmins):
    list_display = ["id", "name", "book_type", "author", "img_link", "desc", "browse_count", ]
    search_fields = ['name', ]
    list_editable = ["name", ]
    list_filter = ["name", ]
    style_fields = {"catalog": "ueditor"}

    object_key = BookDetailMsgs.object_header_cache_key + "*"
    list_key = BookDetailMsgs.list_header_cache_key + "*"



xadmin.site.register(BookType, BookTypeAdmin)
xadmin.site.register(BookAuthor, BookAuthorAdmin)
xadmin.site.register(BookDetail, BookDetailAdmin)
