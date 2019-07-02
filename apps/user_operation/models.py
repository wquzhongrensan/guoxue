from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from forums.models import ForumTopic

User = get_user_model()


class UserFav(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(User, related_name="user_fav", verbose_name="用户", on_delete=models.CASCADE)
    topic = models.ForeignKey(ForumTopic, related_name="topic_fav", verbose_name="收藏的帖子", help_text="帖子id", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta(object):
        db_table = 'GX_user_fav'
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together = ("user", "topic")

    def __str__(self):
        return '用户收藏信息'


class UseFollow(models.Model):
    """
    用户关注
    """
    user = models.ForeignKey(User, related_name="follower", on_delete=models.CASCADE, verbose_name="用户")
    follow = models.ForeignKey(User, related_name="followed", on_delete=models.CASCADE, help_text="用户id", verbose_name="关注的用户")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta(object):
        db_table = 'GX_user_follow'
        verbose_name = '用户关注'
        verbose_name_plural = verbose_name
        unique_together = ("user", "follow")

    def __str__(self):
        return '用户关注信息'
