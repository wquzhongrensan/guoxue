from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from DjangoUeditor.models import UEditorField

# 获取user模型类对象
User = get_user_model()


class ForumType(models.Model):
    """
    论坛版块分类
    """
    Forum_Type = (
        (1, "一级类目"),
        (2, "二级类目"),
    )
    title = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    forum_type = models.IntegerField(choices=Forum_Type, verbose_name="类目级别", help_text="类目级别")
    parent_forum = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_forum", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta(object):
        db_table = "GX_forum_type"
        verbose_name = "论坛版块类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ForumTopic(models.Model):
    """
    论坛帖子主题表
    """
    title = models.CharField(default="", max_length=50, verbose_name="帖子标题", help_text="帖子标题")
    forum_type = models.ForeignKey(ForumType, related_name="forum_topic",help_text="帖子类型", on_delete=models.CASCADE, verbose_name="所属类别")
    author = models.ForeignKey(User, related_name="author_forum", on_delete=models.CASCADE,help_text="帖子作者", verbose_name="作者")
    browse_count = models.IntegerField(default=0, null=True, blank=True, verbose_name="浏览量", help_text="帖子浏览量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    last_reply_time = models.DateTimeField(auto_now=True, verbose_name="最后发表时间")

    class Meta(object):
        db_table = "GX_forum_topic"
        verbose_name = "帖子主题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ForumContent(models.Model):
    """
    论坛帖子内容表
    """
    topic = models.ForeignKey(ForumTopic, default='', related_name="forum_content", on_delete=models.CASCADE, verbose_name="所属帖子主题")
    content = UEditorField(verbose_name="帖子内容", imagePath="forums/images/", width=1000, height=300,
                              filePath="forums/files/", default='')

    class Meta(object):
        db_table = "GX_forum_content"
        verbose_name = "帖子内容详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '内容'


class ForumReply(models.Model):
    """
    论坛回复表
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="回复人")
    topic = models.ForeignKey(ForumTopic, related_name="forum_reply", on_delete=models.CASCADE, verbose_name="所属帖子主题")
    content = UEditorField(verbose_name="回复内容", imagePath="forums/images/", width=1000, height=300,
                           filePath="forums/files/", default='')

    add_time = models.DateTimeField(default=datetime.now, verbose_name="回复时间")
    last_reply_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta(object):
        db_table = "GX_forum_reply"
        verbose_name = "帖子回复"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.author.username
