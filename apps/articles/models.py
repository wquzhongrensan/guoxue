from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField


class ArticleType(models.Model):
    """
    文章分类
    1)诗词清话 5类 （热门文章当做一类）
    2)哲学文化 4类
    3)经济史论 6类
    4)国学人物 --人物春秋归结到这里的文章分类来，然后人物介绍则是分开的
    5)其他
     --今日国学、国学入门
    """
    Article_Type = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )

    title = models.CharField(null=True, max_length=30, verbose_name="类别名", help_text="类别名")
    type_desc = models.CharField(null=True, blank=True, max_length=300, verbose_name="类别描述信息")
    article_types = models.IntegerField(choices=Article_Type, verbose_name="类目级别", help_text="类目级别")
    parent_article = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_acticle", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta(object):
        db_table = "GX_article_type"
        verbose_name = "文章分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Article(models.Model):
    """
    文章详情
    """
    title = models.CharField(max_length=50, verbose_name="标题")
    article_type = models.ForeignKey(ArticleType, related_name="article", on_delete=models.CASCADE, verbose_name="所属类别")
    author_name = models.CharField(null=True, blank=True, max_length=20, verbose_name="作者姓名")
    author_link = models.CharField(null=True, blank=True, max_length=30, verbose_name="作者简介链接")
    img_link = models.ImageField(null=True, blank=True, upload_to='daodus/book_images', verbose_name="文章图片")
    browse_count = models.IntegerField(default=0, blank=True, verbose_name="浏览量")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta(object):
        db_table = "GX_article"
        verbose_name = "文章详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ArticleContent(models.Model):
    """
    文章内容
    """
    article = models.ForeignKey(Article, related_name="article_content", on_delete=models.CASCADE, verbose_name="所属文章")
    content = UEditorField(verbose_name="文章内容", imagePath="articles/images/", width=1000, height=300,
                           filePath="article/files/", default='')

    class Meta(object):
        db_table = "GX_article_content"
        verbose_name = "文章内容"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.article.title


class Person(models.Model):
    """
    国学人物介绍
    """
    name = models.CharField(max_length=20, verbose_name="姓名")
    article_type = models.ForeignKey(ArticleType, related_name="person", null=True, on_delete=models.CASCADE, verbose_name="所属类别")
    img_link = models.ImageField(upload_to='article/images', null=True, blank=True, verbose_name="人物头像")
    birth_place = models.CharField(max_length=20, null=True, blank=True, verbose_name="籍贯")
    life_time = models.CharField(max_length=50, null=True, blank=True, verbose_name="生卒")
    desc = models.CharField(max_length=50, null=True, blank=True, verbose_name="简述")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta(object):
        db_table = "GX_person"
        verbose_name = "国学人物介绍"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class PersonContent(models.Model):
    """
    人物介绍
    """
    person = models.ForeignKey(Person, null=True, related_name="person_content", on_delete=models.CASCADE, verbose_name="所属人物")
    content = UEditorField(verbose_name="人物生平", imagePath="articles/images/", width=1000, height=300,
                           filePath="article/files/", default='')

    class Meta(object):
        db_table = "GX_person_content"
        verbose_name = "人物介绍"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.person.name
