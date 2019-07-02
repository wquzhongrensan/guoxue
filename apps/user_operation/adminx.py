import xadmin

from djcelery.models import (TaskState, WorkerState,PeriodicTask,
                             IntervalSchedule, CrontabSchedule,PeriodicTasks)

from .models import UserFav, UseFollow


class UserFavAdmin(object):
    list_display = ["id", "user", "topic"]
    search_fields = ['user']
    list_editable = ["user"]
    list_filter = ["user"]


class UseFollowAdmin(object):
    list_display = ["id", "user", "follow"]
    search_fields = ['user']
    list_editable = ["user"]
    list_filter = ["user"]

xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UseFollow, UseFollowAdmin)


# celery  --- 后台管理定时任务
xadmin.site.register(IntervalSchedule) # 存储循环任务设置的时间
xadmin.site.register(CrontabSchedule) # 存储定时任务设置的时间
xadmin.site.register(PeriodicTask) # 存储任务
xadmin.site.register(TaskState) # 存储任务执行状态
xadmin.site.register(WorkerState) # 存储执行任务的worker
xadmin.site.register(PeriodicTasks)
