import xadmin

from .models import UserProfile


class UserProfileAdmin(object):
    list_display = ['id', 'username', 'email']  # 添加要显示的列
    search_fields = ['id', 'username', 'email']  # 要查询的列
    list_filter = ['id', 'username', 'email']  # 要筛选的列

xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)
