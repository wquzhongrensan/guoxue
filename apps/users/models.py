from datetime import datetime

from django.db import models

from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """用户信息表"""

    name = models.CharField(max_length=20, null=True, blank=True, verbose_name="昵称")
    img_link = models.ImageField(upload_to='users',default='/users/users1.gif', null=True, blank=True, verbose_name="作者头像")
    gender = models.CharField(max_length=6, null=True, blank=True, choices=(("male", "男"), ("female", "女")), verbose_name="性别")
    birthday = models.DateTimeField(null=True, blank=True, verbose_name="出生日期")
    email = models.CharField(max_length=30, null=True, blank=True, verbose_name="邮箱")
    area = models.CharField(max_length=20,null=True, blank=True, verbose_name="所在城市")
    introduce = models.CharField(max_length=100, null=True, blank=True, verbose_name="简介")
    attention = models.IntegerField(default=0, null=True, blank=True ,verbose_name="关注数")
    fans = models.IntegerField(default=0, null=True, blank=True, verbose_name="粉丝数")
    total_grade = models.IntegerField(default=0, null=True, blank=True, verbose_name="总积分")
    current_sort = models.IntegerField(null=True, blank=True, verbose_name="当前排名")
    publish_post = models.IntegerField(default=0, null=True, blank=True, verbose_name="发帖数")
    publish_reply = models.IntegerField(default=0, null=True, blank=True, verbose_name="回帖数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta(object):
        db_table = "GX_user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
