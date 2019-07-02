import xadmin
from xadmin import views
from django.core.cache import cache

from .models import ArticleType, Article, ArticleContent, Person, PersonContent


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class BaseAdmins(object):

    object_key = "Article*"
    list_key = "Article*"

    def save_models(self):
        cache.delete_pattern(self.object_key)
        cache.delete_pattern(self.list_key)
        super().save_models()


class GlobalSettings(object):
    site_title = "国学之家后台"
    site_footer = "guoxue"
    # menu_style = "accordion"


class ArticleTypeAdmin(BaseAdmins):
    list_display = ["id", "title", "type_desc", "article_types", "parent_article"]
    search_fields = ['title', ]
    list_editable = ["title", ]
    list_filter = ["title",]

    class ArticleTypeInline(BaseAdmins):
        model = ArticleType
        exclude = ["add_time"]
        extra = 1
        style = 'tab'

    class ArticleInline(BaseAdmins):
        model = Article
        exclude = ["add_time"]
        extra = 1
        style = 'tab'

    inlines = [ArticleInline, ArticleTypeInline]


class ArticleAdmin(BaseAdmins):
    list_display = ["id", "title", "article_type", "author_name", "author_link", "img_link", "browse_count"]
    search_fields = ['title', ]
    list_editable = ["title", ]
    list_filter = ["title", ]

    class ArticleContentInline(BaseAdmins):
        model = ArticleContent
        exclude = ["add_time"]
        extra = 1
        style = 'tab'
    inlines = [ArticleContentInline, ]


class ArticleContentAdmin(BaseAdmins):
    list_display = ["id", "content", "article"]
    style_fields = {"content": "ueditor"}
    search_fields = ['content', ]
    list_editable = ["content", ]
    list_filter = ["content", ]


class PersonAdmin(BaseAdmins):
    list_display = ["id", "name", "article_type", "img_link", "birth_place", "life_time", "desc"]
    search_fields = ['name', ]
    list_editable = ["name", ]
    list_filter = ["name", ]

    class PersonContentInline(BaseAdmins):
        model = PersonContent
        exclude = ["add_time"]
        extra = 1
        style = 'tab'

    inlines = [PersonContentInline, ]


class PersonContentAdmin(BaseAdmins):
    list_display = ["id", "person", "content",]
    style_fields = {"content": "ueditor"}
    search_fields = ['content', ]
    list_filter = ["content", ]


xadmin.site.register(ArticleType, ArticleTypeAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(ArticleContent, ArticleContentAdmin)
xadmin.site.register(Person, PersonAdmin)
xadmin.site.register(PersonContent, PersonContentAdmin)

# xadmin后台的基本配置
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
