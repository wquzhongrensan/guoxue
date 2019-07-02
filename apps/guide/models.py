from django.db import models
from datetime import datetime


class GuideType(models.Model):
    """
    国学指南之版块分类
    """
    Guide_Type = (
        (1, "一级类目"),
        (2, "二级类目"),
    )

    title = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    guide_type = models.IntegerField(choices=Guide_Type, verbose_name="类目级别", help_text="类目级别")
    parent_guide = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_guide", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta(object):
        db_table = "GX_guide_type"
        verbose_name = "国学指南之版块类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class GuideDetail(models.Model):
    """指南详情"""
    title = models.CharField(max_length=10, verbose_name="指南title", help_text="指南title")
    link = models.CharField(max_length=100, verbose_name="指南链接", help_text="指南链接")
    guide_type = models.ForeignKey(GuideType, default='', on_delete=models.CASCADE, related_name="guide_detail", verbose_name="所属类别")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta(object):
        db_table = "GX_guide_detail"
        verbose_name = "国学指南值详情信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
