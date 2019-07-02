import xadmin

from .models import GuideDetail, GuideType


class GuideTypeAdmin(object):
    list_display = ["id", "title", "guide_type", "parent_guide", ]
    search_fields = ['title', ]
    list_editable = ["title", ]
    list_filter = ["title", ]

    class GuideDetailInline(object):
        model = GuideDetail
        exclude = ["add_time"]
        extra = 1
        style = 'tab'

    inlines = [GuideDetailInline]


class GuideDetailAdmin(object):
    list_display = ["title", "link" ]
    search_fields = ['title', ]
    list_editable = ["title", ]
    list_filter = ["title", ]


xadmin.site.register(GuideType, GuideTypeAdmin)
xadmin.site.register(GuideDetail, GuideDetailAdmin)
