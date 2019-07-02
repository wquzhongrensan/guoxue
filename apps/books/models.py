from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField


class BookType(models.Model):
    """
    经典导读--书籍版块分类
    """
    Book_Type = (
        (1, "一级类目"),
        (2, "二级类目"),
    )

    title = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    desc = models.CharField(null=True, blank=True, max_length=300, verbose_name="类别描述信息")
    book_type = models.IntegerField(choices=Book_Type, verbose_name="类目级别", help_text="类目级别")
    parent_forum = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_book", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta(object):
        db_table = "GX_book_type"
        verbose_name = "书籍版块类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class BookAuthor(models.Model):
    """
    经典导读--书籍作者信息
    """
    name = models.CharField(max_length=20, verbose_name="作者姓名")
    introduce_link = models.CharField(max_length=30, verbose_name="作者简介链接")
    introduces = models.CharField(max_length=300, verbose_name="作者简介")
    avatar_link = models.ImageField(upload_to='daodus/avatar_imgs', null=True, blank=True, verbose_name="作者头像")

    class Meta(object):
        db_table = "GX_book_author"
        verbose_name = "书籍作者详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BookDetail(models.Model):
    """
    经典导读--书籍详情
    """
    name = models.CharField(max_length=50, verbose_name="书名")
    book_type = models.ForeignKey(BookType, related_name="book", on_delete=models.CASCADE, verbose_name="所属类别")
    author = models.ForeignKey(BookAuthor, verbose_name="作者", related_name="author_book", on_delete=models.CASCADE)
    img_link = models.ImageField(upload_to='daodus/book_images', null=True, blank=True, verbose_name="书籍图片")
    desc = models.CharField(max_length=500, verbose_name="书籍描述信息")
    browse_count = models.IntegerField(default=0, null=True, blank=True, verbose_name="浏览量")
    publishing_house = models.CharField(max_length=20,null=True, blank=True, verbose_name="出版社")
    publishing_date = models.DateField(verbose_name="出版日期",null=True, blank=True,)
    page_count = models.IntegerField(verbose_name="页数",null=True, blank=True,)
    price = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True, verbose_name="定价")
    IBSN = models.CharField(max_length=20, verbose_name="书籍IBSN号码",null=True, blank=True,)
    catalog = UEditorField(verbose_name="书籍目录", width=1000,null=True, blank=True, height=300, default='')

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta(object):
        db_table = "GX_book_detail"
        verbose_name = "书籍详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
